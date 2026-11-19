#!/usr/bin/env python3
"""Trace downstream knowledge objects affected by a source change.

This is an impact aid, not an automatic scientific invalidation mechanism.
Canonical registries remain the source of truth; graph edges are reported as
context and are never traversed to infer epistemic consequences.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_FILES = {
    "SOURCE": ("sources/registry.yml", "sources"),
    "STUDY": ("research/studies/registry.yml", "studies"),
    "DATASET": ("research/datasets/registry.yml", "datasets"),
    "CLAIM": ("claims/registry.yml", "claims"),
    "HYPOTHESIS": ("hypotheses/registry.yml", "hypotheses"),
    "DOSSIER": ("dossiers/registry.yml", "dossiers"),
    "CONCEPT": ("knowledge/concepts/registry.yml", "concepts"),
    "MECHANISM": ("knowledge/mechanisms/registry.yml", "mechanisms"),
    "FORECAST": ("forecasts/registry.yml", "forecasts"),
}

# Explicit typed references only. Domain/tag co-membership is deliberately
# excluded: it is classification, not evidence of downstream dependency.
REFERENCE_FIELDS = {
    "STUDY": {"SOURCE": ("source_ids",)},
    "DATASET": {"SOURCE": ("source_ids",)},
    "CLAIM": {
        "SOURCE": ("source_ids",),
        "STUDY": ("study_ids",),
        "DATASET": ("dataset_ids",),
    },
    "HYPOTHESIS": {"STUDY": ("supporting_study_ids", "challenging_study_ids")},
    "DOSSIER": {
        "CLAIM": ("claim_ids",),
        "STUDY": ("study_ids",),
        "HYPOTHESIS": ("hypothesis_ids",),
        "CONCEPT": ("concept_ids",),
    },
}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream) or {}


def record_references(
    record: dict[str, Any],
    fields: tuple[str, ...],
    *,
    include_source_verifications: bool = False,
) -> set[str]:
    found: set[str] = set()
    for field in fields:
        values = record.get(field, []) or []
        if isinstance(values, str):
            found.add(values)
        elif isinstance(values, list):
            found.update(value for value in values if isinstance(value, str))
    # Claim-level source verification references are first-class dependencies,
    # but must never be interpreted as a generic field on other object types.
    if include_source_verifications:
        for verification in record.get("source_verifications", []) or []:
            if isinstance(verification, dict) and isinstance(verification.get("source_id"), str):
                found.add(verification["source_id"])
    return found


def index_records(registries: dict[str, list[dict[str, Any]]]) -> dict[str, dict[str, dict[str, Any]]]:
    return {
        kind: {item["id"]: item for item in items if isinstance(item, dict) and isinstance(item.get("id"), str)}
        for kind, items in registries.items()
    }


def find_dependents(
    registries: dict[str, list[dict[str, Any]]],
    impacted: dict[str, set[str]],
    dependent_kind: str,
    target_kind: str,
    source_kinds: tuple[str, ...],
) -> set[str]:
    """Return dependents of one requested type, avoiding cross-type ID leakage."""
    fields = REFERENCE_FIELDS.get(dependent_kind, {}).get(target_kind)
    if not fields:
        return set()
    found: set[str] = set()
    for record in registries.get(dependent_kind, []):
        refs = record_references(
            record,
            fields,
            include_source_verifications=(dependent_kind == "CLAIM" and target_kind == "SOURCE"),
        )
        if any(refs & impacted.get(kind, set()) for kind in source_kinds):
            found.add(record["id"])
    return found


def build_impact_report(
    registries: dict[str, list[dict[str, Any]]],
    graph_edges: list[dict[str, Any]],
    synthesis_entries: list[dict[str, Any]],
    source_id: str,
) -> dict[str, Any]:
    index = index_records(registries)
    if source_id not in index.get("SOURCE", {}):
        raise ValueError(f"Unknown source id: {source_id}")

    impacted: dict[str, set[str]] = {kind: set() for kind in registries}
    impacted["SOURCE"] = {source_id}
    # Level 1: objects directly tied to the source.
    for kind in ("STUDY", "DATASET", "CLAIM"):
        fields = REFERENCE_FIELDS.get(kind, {}).get("SOURCE", ())
        for record in registries.get(kind, []):
            if source_id in record_references(
                record,
                fields,
                include_source_verifications=(kind == "CLAIM"),
            ):
                impacted.setdefault(kind, set()).add(record["id"])

    # Level 2: claims using impacted studies/datasets; hypotheses using studies.
    for kind in ("STUDY", "DATASET"):
        impacted.setdefault("CLAIM", set()).update(
            find_dependents(registries, impacted, "CLAIM", kind, (kind,))
        )
    impacted.setdefault("HYPOTHESIS", set()).update(
        find_dependents(registries, impacted, "HYPOTHESIS", "STUDY", ("STUDY",))
    )

    # Level 3: dossiers explicitly referencing affected knowledge objects.
    for kind in ("CLAIM", "STUDY", "HYPOTHESIS"):
        impacted.setdefault("DOSSIER", set()).update(
            find_dependents(registries, impacted, "DOSSIER", kind, (kind,))
        )

    synthesis_by_dossier: dict[str, list[dict[str, str]]] = {}
    for entry in synthesis_entries:
        if not isinstance(entry, dict):
            continue
        dossier_id = entry.get("dossier_id")
        if dossier_id in impacted.get("DOSSIER", set()):
            synthesis_by_dossier.setdefault(dossier_id, []).append({
                "synthesis_id": entry.get("synthesis_id", ""),
                "synthesis_path": entry.get("synthesis_path", ""),
            })

    impacted_ids = {identifier for values in impacted.values() for identifier in values}
    # Graph is contextual only: report incident edges; do not traverse them.
    related_edges = [
        edge for edge in graph_edges
        if edge.get("from") in impacted_ids or edge.get("to") in impacted_ids
    ]

    records_out = {}
    for kind, identifiers in impacted.items():
        if not identifiers:
            continue
        records_out[kind] = [
            {
                "id": identifier,
                "title": index.get(kind, {}).get(identifier, {}).get("title")
                    or index.get(kind, {}).get(identifier, {}).get("label")
                    or index.get(kind, {}).get(identifier, {}).get("statement", ""),
            }
            for identifier in sorted(identifiers)
        ]

    return {
        "source_id": source_id,
        "records": records_out,
        "syntheses": [
            {"dossier_id": dossier_id, **item}
            for dossier_id, items in sorted(synthesis_by_dossier.items())
            for item in items
        ],
        "graph_edges": [
            {
                "id": edge.get("id", ""),
                "type": edge.get("type", ""),
                "from": edge.get("from", ""),
                "to": edge.get("to", ""),
                "justification": edge.get("justification", ""),
            }
            for edge in sorted(related_edges, key=lambda item: item.get("id", ""))
        ],
        "scope_note": (
            "Impact indicatif fondé sur les références typées explicites. "
            "Les arêtes du graphe sont affichées comme contexte, sans propagation. "
            "Une présence dans ce rapport signale une revue à effectuer, pas une "
            "invalidité automatique ni une modification scientifique. "
            "L'absence de lien explicite détecté ne démontre pas l'absence de "
            "dépendance réelle : des références peuvent être manquantes ou non typées."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# Analyse d’impact — {report['source_id']}",
        "",
        report["scope_note"],
        "",
    ]
    labels = {
        "STUDY": "Études directement liées",
        "DATASET": "Jeux de données directement liés",
        "CLAIM": "Claims concernés",
        "HYPOTHESIS": "Hypothèses concernées",
        "DOSSIER": "Dossiers à revoir",
    }
    for kind, label in labels.items():
        items = report["records"].get(kind, [])
        lines.extend([f"## {label}", ""])
        if items:
            lines.extend(f"- `{item['id']}` — {item['title']}" for item in items)
        else:
            lines.append("- Aucun lien explicite détecté.")
        lines.append("")
    lines.extend(["## Synthèses associées", ""])
    if report["syntheses"]:
        lines.extend(
            f"- `{item['synthesis_id']}` — `{item['synthesis_path']}` "
            f"(dossier `{item['dossier_id']}`)"
            for item in report["syntheses"]
        )
    else:
        lines.append("- Aucune synthèse associée via le registre.")
    lines.extend(["", "## Arêtes du graphe incidentes", ""])
    if report["graph_edges"]:
        lines.extend(
            f"- `{edge['id']}` ({edge['type']}) : `{edge['from']}` → "
            f"`{edge['to']}` — {edge['justification']}"
            for edge in report["graph_edges"]
        )
    else:
        lines.append("- Aucune arête incidente.")
    lines.extend([
        "",
        "## Décision humaine requise",
        "",
        "Vérifier chaque dépendance sur la source et son localisateur. "
        "Décider explicitement si elle est inchangée, à recontrôler, à corriger "
        "ou à déprécier ; ne pas propager mécaniquement un changement de statut.",
        "",
    ])
    return "\n".join(lines)


def load_repository(root: Path) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]], list[dict[str, Any]]]:
    registries = {}
    for kind, (relative, collection) in REGISTRY_FILES.items():
        path = root / relative
        if path.exists():
            registries[kind] = load_yaml(path).get(collection, [])
        else:
            registries[kind] = []
    graph = load_yaml(root / "knowledge/graph.yml").get("relations", [])
    synthesis = load_yaml(root / "syntheses/registry.yml").get("dossiers", [])
    return registries, graph, synthesis


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-id", required=True, help="Canonical SOURCE identifier")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()
    registries, graph, syntheses = load_repository(ROOT)
    try:
        report = build_impact_report(registries, graph, syntheses, args.source_id)
    except ValueError as exc:
        parser.error(str(exc))
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
