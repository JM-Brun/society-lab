#!/usr/bin/env python3
"""Trace downstream knowledge objects affected by a source change.

This is an impact aid, not an automatic scientific invalidation mechanism.
Canonical registries remain the source of truth; graph edges are reported as
context and are never traversed to infer epistemic consequences.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
LIFECYCLE_PATH = "sources/lifecycle.yml"
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
    "MECHANISM": {
        "STUDY": ("supporting_study_ids", "challenging_study_ids"),
        "CLAIM": ("claim_ids",),
    },
    "FORECAST": {"CLAIM": ("claim_ids",)},
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

    # Level 3: explanatory mechanisms and forecasts explicitly tied to
    # affected studies or claims. Their own typed references are not inferred
    # from graph edges or domain co-membership.
    for target_kind in ("STUDY", "CLAIM"):
        impacted.setdefault("MECHANISM", set()).update(
            find_dependents(registries, impacted, "MECHANISM", target_kind, (target_kind,))
        )
    impacted.setdefault("FORECAST", set()).update(
        find_dependents(registries, impacted, "FORECAST", "CLAIM", ("CLAIM",))
    )

    # Level 4: dossiers explicitly referencing affected knowledge objects.
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
            "invalidité automatique ni une modification scientifique."
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
        "MECHANISM": "Mécanismes explicatifs à revoir",
        "FORECAST": "Prévisions dépendantes à réexaminer",
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


def git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args], cwd=root, check=True, capture_output=True, encoding="utf-8",
    )
    return result.stdout


def load_git_yaml(root: Path, revision: str, relative: str) -> dict[str, Any]:
    return yaml.safe_load(git(root, "show", f"{revision}:{relative}")) or {}


def load_repository(
    root: Path, *, revision: str | None = None,
) -> tuple[dict[str, list[dict[str, Any]]], list[dict[str, Any]], list[dict[str, Any]]]:
    paths = [relative for relative, _ in REGISTRY_FILES.values()]
    if revision is None:
        files = {relative for relative in paths if (root / relative).exists()}
    else:
        files = set(git(root, "ls-tree", "-r", "--name-only", revision, "--", *paths).splitlines())

    def read(relative: str) -> dict[str, Any]:
        if revision is None:
            return load_yaml(root / relative)
        return load_git_yaml(root, revision, relative)

    registries = {}
    for kind, (relative, collection) in REGISTRY_FILES.items():
        registries[kind] = read(relative).get(collection, []) if relative in files else []
    graph = read("knowledge/graph.yml").get("relations", [])
    synthesis = read("syntheses/registry.yml").get("dossiers", [])
    return registries, graph, synthesis


def compare_sources(before: list[dict], after: list[dict]) -> list[dict]:
    previous = index_records({"SOURCE": before})["SOURCE"]
    current = index_records({"SOURCE": after})["SOURCE"]
    if len(previous) != len(before) or len(current) != len(after):
        raise ValueError("Source records must have distinct string identifiers in both revisions")

    changes = []
    missing = object()
    for source_id in sorted(previous.keys() | current.keys()):
        if source_id not in previous:
            changes.append({"source_id": source_id, "change": "added"})
        elif source_id not in current:
            changes.append({"source_id": source_id, "change": "removed"})
        else:
            old, new = previous[source_id], current[source_id]
            fields = [key for key in sorted(old.keys() | new.keys()) if old.get(key, missing) != new.get(key, missing)]
            if fields:
                changes.append({"source_id": source_id, "change": "modified", "changed_fields": fields})
    return changes


def build_git_impact_report(root: Path, base: str, revision: str) -> dict:
    before_ref, after_ref = (
        git(root, "rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}").strip()
        for ref in (base, revision)
    )
    path, collection = REGISTRY_FILES["SOURCE"]
    before = load_git_yaml(root, before_ref, path)[collection]
    after = load_git_yaml(root, after_ref, path)[collection]
    changes = compare_sources(before, after)
    for label, ref, absent in (("before", before_ref, "added"), ("after", after_ref, "removed")):
        relevant = [entry for entry in changes if entry["change"] != absent]
        if relevant:
            snapshot = load_repository(root, revision=ref)
            for entry in relevant:
                entry[f"impact_{label}"] = build_impact_report(*snapshot, entry["source_id"])
    return {"base_revision": before_ref, "revision": after_ref, "sources": changes}


def impact_counts(impact: dict | None) -> str:
    if impact is None:
        return "—"
    records = sum(len(rows) for kind, rows in impact["records"].items() if kind != "SOURCE")
    syntheses = len({row["synthesis_id"] for row in impact["syntheses"]})
    return f"{records} / {syntheses}"


def build_event_impact_report(root: Path, event_id: str, revision: str | None = None) -> dict:
    if revision is None:
        journal = load_yaml(root / LIFECYCLE_PATH)
    else:
        revision = git(root, "rev-parse", "--verify", "--end-of-options", f"{revision}^{{commit}}").strip()
        journal = load_git_yaml(root, revision, LIFECYCLE_PATH)

    matches = [event for event in journal["events"] if event["id"] == event_id]
    if len(matches) != 1:
        raise ValueError(f"Expected one event with id {event_id}, found {len(matches)}")
    event = matches[0]
    current = load_repository(root, revision=revision)
    impacts = {"current": build_impact_report(*current, event["source_id"])}
    if "replacement_source_id" in event:
        impacts["replacement"] = build_impact_report(*current, event["replacement_source_id"])
    if baseline := event.get("baseline_revision"):
        previous = load_repository(root, revision=baseline)
        impacts["baseline"] = build_impact_report(*previous, event["source_id"])

    targets = {
        record["id"]
        for impact in impacts.values()
        for records in impact["records"].values()
        for record in records
    }
    targets.update(row["synthesis_id"] for impact in impacts.values() for row in impact["syntheses"])
    decisions = {decision["target_id"] for decision in event["decisions"]}
    return {
        "revision": revision,
        "event": event,
        "impacts": impacts,
        "targets_without_decision": sorted(targets - decisions),
        "decisions_outside_detected_impact": sorted(decisions - targets),
    }


def render_event_markdown(report: dict) -> str:
    event = report["event"]
    evidence = event["evidence"]
    lines = [
        f"# Revue de source — {event['id']}", "",
        f"`{event['source_id']}` · `{event['kind']}` · {event['recorded_on']}", "",
        event["summary"], "",
        f"Pièce : {evidence['locator']} <{evidence['url']}>", "",
        f"Révision du journal et du corpus : {report['revision'] or 'copie de travail'}.",
    ]
    if event.get("baseline_revision"):
        lines.append(f"Révision avant l'événement : `{event['baseline_revision']}`.")
    for heading, key in (
        ("Cibles détectées sans décision", "targets_without_decision"),
        ("Décisions hors des dépendances détectées", "decisions_outside_detected_impact"),
    ):
        lines.extend(["", f"## {heading}", ""])
        lines.extend(f"- `{identifier}`" for identifier in report[key])
        if not report[key]:
            lines.append("- Aucune.")
    lines.extend(["", "## Décisions consignées", ""])
    lines.extend(
        f"- `{item['target_id']}` · `{item['status']}` · {item['reviewed_on']} — {item['reason']}"
        for item in sorted(event["decisions"], key=lambda item: item["target_id"])
    )
    if not event["decisions"]:
        lines.append("- Aucune.")
    return "\n".join(lines)


def render_git_markdown(report: dict) -> str:
    changes = report["sources"]
    lines = [
        "## Impact des modifications de sources", "",
        f"Comparaison de `{report['base_revision']}` à `{report['revision']}`.",
        f"**Fiches sources ajoutées, retirées ou modifiées** · {len(changes)}", "",
    ]
    if changes:
        lines.extend([
            "Les nombres indiquent les objets liés et les synthèses distinctes à examiner par source.", "",
            "| Source | Changement | Champs modifiés | Objets / synthèses avant | Objets / synthèses après |",
            "|---|---|---|---:|---:|",
        ])
        labels = {"added": "Ajoutée", "removed": "Retirée", "modified": "Modifiée"}
        for entry in changes[:30]:
            fields = ", ".join(f"`{field}`" for field in entry.get("changed_fields", [])) or "—"
            lines.append(
                f"| `{entry['source_id']}` | {labels[entry['change']]} | {fields} | "
                f"{impact_counts(entry.get('impact_before'))} | {impact_counts(entry.get('impact_after'))} |"
            )
        if len(changes) > 30:
            lines.extend(["", "Le résumé affiche les 30 premières sources. Le JSON contient la liste complète."])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--source-id", help="Canonical SOURCE identifier in the working tree")
    mode.add_argument("--base", help="Base Git revision for source change detection")
    mode.add_argument("--event-id", help="Lifecycle event identifier")
    parser.add_argument("--revision", help="Git revision for --base or --event-id")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--json-output", type=Path, help="Also write the JSON report to this path")
    args = parser.parse_args()
    if args.revision is not None and args.source_id is not None:
        parser.error("--revision requires --base or --event-id")
    try:
        if args.event_id is not None:
            report = build_event_impact_report(ROOT, args.event_id, args.revision)
            render = render_event_markdown
        elif args.source_id is not None:
            report = build_impact_report(*load_repository(ROOT), args.source_id)
            render = render_markdown
        else:
            report = build_git_impact_report(ROOT, args.base, args.revision or "HEAD")
            render = render_git_markdown
        serialized = json.dumps(report, ensure_ascii=False, indent=2)
        if args.json_output:
            args.json_output.write_text(serialized + "\n", encoding="utf-8")
    except subprocess.CalledProcessError as exc:
        parser.error(exc.stderr.strip() or "unable to read the requested Git revisions")
    except (KeyError, OSError, TypeError, ValueError, yaml.YAMLError) as exc:
        parser.error(str(exc))
    print(serialized if args.format == "json" else render(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
