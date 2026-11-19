#!/usr/bin/env python3
"""Calculate auditable, read-only Society Lab project KPIs."""
from __future__ import annotations
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRIES = (
    ("sources/registry.yml", "sources"), ("claims/registry.yml", "claims"),
    ("dossiers/registry.yml", "dossiers"), ("forecasts/registry.yml", "forecasts"),
    ("hypotheses/registry.yml", "hypotheses"),
    ("knowledge/concepts/registry.yml", "concepts"),
    ("knowledge/mechanisms/registry.yml", "mechanisms"),
    ("research/datasets/registry.yml", "datasets"),
    ("research/studies/registry.yml", "studies"),
)
RELATION_TYPES = {"REL-SUPPORTS", "REL-QUALIFIES", "REL-INCLUDES", "REL-USES",
                  "REL-CITES", "REL-TRANSCRIBES", "REL-TRANSCRIBED-FROM"}
CONCLUSIVE_STATUSES = {"supported", "partially_supported", "contested",
                       "not_supported", "insufficient_evidence"}
NON_CONCLUSIVE_STATUSES = {"unexamined", "under_review"}

def read_yaml(root: Path, path: str) -> dict[str, Any]:
    with (root / path).open(encoding="utf-8") as stream:
        data = yaml.safe_load(stream) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected YAML mapping")
    return data

def load_project_data(root: Path = ROOT) -> dict[str, Any]:
    registries = {}
    for path, key in REGISTRIES:
        records = read_yaml(root, path).get(key, [])
        if not isinstance(records, list):
            raise ValueError(f"{path}: {key} must be a list")
        registries[key] = records
    return {
        "registries": registries,
        "domains": read_yaml(root, "knowledge/TAXONOMY.yml").get("domains", []),
        "territories": read_yaml(root, "knowledge/TERRITORIES.yml").get("territories", []),
        "synthesis_entries": read_yaml(root, "syntheses/registry.yml").get("dossiers", []),
        "relations": read_yaml(root, "knowledge/graph.yml").get("relations", []),
        "relation_definitions": read_yaml(root, "knowledge/RELATION_TYPES.yml").get("relations", []),
    }

def build_known_ids(data: dict[str, Any]) -> tuple[set[str], list[str]]:
    known, duplicates = set(), []
    groups = list(data["registries"].values()) + [data["domains"], data["territories"]]
    for records in groups:
        for record in records:
            if not isinstance(record, dict):
                continue
            identifier = record.get("id")
            if isinstance(identifier, str) and identifier:
                if identifier in known:
                    duplicates.append(identifier)
                known.add(identifier)
    # Several dossier rows intentionally share one synthesis_id; only collisions
    # with another node registry are duplicates.
    synthesis_ids = set()
    for row in data["synthesis_entries"]:
        identifier = row.get("synthesis_id") if isinstance(row, dict) else None
        if isinstance(identifier, str) and identifier:
            if identifier in known and identifier not in synthesis_ids:
                duplicates.append(identifier)
            known.add(identifier)
            synthesis_ids.add(identifier)
    return known, sorted(set(duplicates))


def build_node_type_index(data: dict[str, Any]) -> dict[str, str]:
    """Index graph node identifiers by their canonical registry type."""
    registry_types = {
        "sources": "SOURCE", "claims": "CLAIM", "dossiers": "DOSSIER",
        "forecasts": "FORECAST", "hypotheses": "HYPOTHESIS",
        "concepts": "CONCEPT", "mechanisms": "MECHANISM",
        "datasets": "DATASET", "studies": "STUDY",
    }
    node_types = {}
    for collection, node_type in registry_types.items():
        for record in data["registries"].get(collection, []):
            if isinstance(record, dict) and isinstance(record.get("id"), str):
                node_types[record["id"]] = node_type
    for collection, node_type in (("domains", "DOMAIN"), ("territories", "TERRITORY")):
        for record in data.get(collection, []):
            if isinstance(record, dict) and isinstance(record.get("id"), str):
                node_types[record["id"]] = node_type
    for row in data.get("synthesis_entries", []):
        identifier = row.get("synthesis_id") if isinstance(row, dict) else None
        if isinstance(identifier, str) and identifier:
            node_types[identifier] = "SYNTHESIS"
    return node_types

def inspect_relations(relations: list[dict[str, Any]], known_ids: set[str], known_relation_types=None,
                      node_type_by_id=None, relation_definitions=None):
    valid, diagnostics = [], {key: [] for key in (
        "missing_ids", "duplicate_ids", "duplicate_triples", "empty_justifications",
        "unknown_endpoints", "unknown_relation_types", "incompatible_endpoints")}
    definitions = {item.get("id"): item for item in (relation_definitions or [])
                   if isinstance(item, dict) and isinstance(item.get("id"), str)}
    seen_ids, seen_triples = set(), set()
    for edge in relations:
        if not isinstance(edge, dict):
            diagnostics["missing_ids"].append("<non-mapping relation>")
            continue
        edge_id, kind = edge.get("id"), edge.get("type")
        source, target = edge.get("from"), edge.get("to")
        invalid = False
        if not isinstance(edge_id, str) or not edge_id:
            diagnostics["missing_ids"].append(str(edge_id)); invalid = True
        elif edge_id in seen_ids:
            diagnostics["duplicate_ids"].append(edge_id); invalid = True
        else:
            seen_ids.add(edge_id)
        triple = (kind, source, target)
        if triple in seen_triples:
            diagnostics["duplicate_triples"].append(str(edge_id)); invalid = True
        seen_triples.add(triple)
        justification = edge.get("justification")
        if not isinstance(justification, str) or not justification.strip():
            diagnostics["empty_justifications"].append(str(edge_id)); invalid = True
        if source not in known_ids or target not in known_ids:
            diagnostics["unknown_endpoints"].append(str(edge_id)); invalid = True
        if (not isinstance(kind, str) or not kind
                or (known_relation_types is not None and kind not in known_relation_types)):
            diagnostics["unknown_relation_types"].append(str(edge_id)); invalid = True
        definition = definitions.get(kind)
        if definition is not None and node_type_by_id is not None:
            for endpoint, actual_id in (("from", source), ("to", target)):
                actual_type = node_type_by_id.get(actual_id)
                allowed_types = definition.get(endpoint, [])
                if actual_type is not None and actual_type not in allowed_types:
                    diagnostics["incompatible_endpoints"].append(
                        f"{edge_id}:{endpoint}:{actual_type}:{kind}")
                    invalid = True
        if not invalid:
            valid.append(edge)
    return valid, diagnostics

def calculate_source_coverage(sources, relations, known_ids, known_relation_types=None,
                              node_type_by_id=None, relation_definitions=None):
    source_ids = {r["id"] for r in sources if isinstance(r, dict) and isinstance(r.get("id"), str)}
    valid_edges, diagnostics = inspect_relations(
        relations, known_ids, known_relation_types, node_type_by_id, relation_definitions
    )
    covered = {node for edge in valid_edges if edge.get("type") in RELATION_TYPES
               for node in (edge.get("from"), edge.get("to")) if node in source_ids}
    uncovered = sorted(source_ids - covered)
    denominator, numerator = len(source_ids), len(covered)
    return {
        "metric_id": "source_to_knowledge_coverage",
        "status": "computed" if denominator else "not_computable",
        "numerator": numerator if denominator else None,
        "denominator": denominator if denominator else None,
        "value": 100 * numerator / denominator if denominator else None,
        "unit": "%",
        "scope": "Toutes les sources du registre ; relations documentaires typées, justifiées et reliées à des objets connus.",
        "excluded_count": 0,
        "unknown_count": sum(map(len, diagnostics.values())),
        "issues": {k: v for k, v in diagnostics.items() if v},
        "covered_source_ids": sorted(covered),
        "uncovered_source_ids": uncovered,
        "definition_version": 1,
    }

def calculate_claim_conclusion_coverage(claims):
    counts, active, unknown = {}, [], []
    for claim in claims:
        if not isinstance(claim, dict):
            unknown.append("<non-mapping claim>"); continue
        status = claim.get("status")
        label = status if isinstance(status, str) and status else "<missing>"
        counts[label] = counts.get(label, 0) + 1
        if status == "superseded":
            continue
        active.append(claim)
        if status not in CONCLUSIVE_STATUSES | NON_CONCLUSIVE_STATUSES:
            unknown.append(str(claim.get("id", "<missing id>")))
    numerator, denominator = sum(c.get("status") in CONCLUSIVE_STATUSES for c in active), len(active)
    return {
        "metric_id": "claim_conclusion_coverage",
        "status": "computed" if denominator else "not_computable",
        "numerator": numerator if denominator else None,
        "denominator": denominator if denominator else None,
        "value": 100 * numerator / denominator if denominator else None,
        "unit": "%",
        "scope": "Claims actifs ; superseded exclus du numérateur et du dénominateur.",
        "excluded_count": len(claims) - denominator,
        "unknown_count": len(unknown),
        "issues": {"unknown_or_missing_status": unknown} if unknown else {},
        "status_counts": counts,
        "active_claim_ids": sorted(str(c.get("id")) for c in active if c.get("id")),
        "conclusive_claim_ids": sorted(str(c.get("id")) for c in active
                                        if c.get("status") in CONCLUSIVE_STATUSES and c.get("id")),
        "superseded_claim_ids": sorted(str(c.get("id")) for c in claims
                                        if isinstance(c, dict) and c.get("status") == "superseded" and c.get("id")),
        "definition_version": 1,
    }


def calculate_synthesis_coverage(dossiers, entries, root: Path):
    """Measure active dossier coverage; shared synthesis files are intentional."""
    active_statuses = {"scoping", "researching", "draft", "under_review", "published"}
    active = [d for d in dossiers if isinstance(d, dict) and d.get("status") != "archived"]
    dossier_ids = {d.get("id") for d in dossiers if isinstance(d, dict) and isinstance(d.get("id"), str)}
    by_dossier = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        by_dossier.setdefault(entry.get("dossier_id"), []).append(entry)

    covered, uncovered, issues = set(), [], {}
    def issue(key, value):
        issues.setdefault(key, []).append(value)

    for dossier in active:
        dossier_id = dossier.get("id", "<missing dossier id>")
        status = dossier.get("status")
        if status not in active_statuses:
            issue("unknown_dossier_status", str(dossier_id))
        matches = by_dossier.get(dossier_id, [])
        if len(matches) != 1:
            uncovered.append(str(dossier_id))
            issue("missing_or_duplicate_mapping", str(dossier_id))
            continue
        entry = matches[0]
        dossier_path = entry.get("dossier_path")
        synthesis_path = entry.get("synthesis_path")
        synthesis_id = entry.get("synthesis_id")
        if not isinstance(dossier_path, str) or not (root / dossier_path).is_file():
            uncovered.append(str(dossier_id))
            issue("missing_dossier_file", str(dossier_id))
            continue
        if not isinstance(synthesis_id, str) or not synthesis_id:
            uncovered.append(str(dossier_id))
            issue("missing_synthesis_id", str(dossier_id))
            continue
        if not isinstance(synthesis_path, str) or not (root / synthesis_path).is_file():
            uncovered.append(str(dossier_id))
            issue("missing_synthesis_file", str(dossier_id))
            continue
        covered.add(dossier_id)

    unknown_mappings = sorted(
        str(entry.get("dossier_id")) for entry in entries
        if isinstance(entry, dict) and entry.get("dossier_id") not in dossier_ids
    )
    if unknown_mappings:
        issue("mapping_without_active_dossier", unknown_mappings)

    denominator, numerator = len(active), len(covered)
    unique_paths = {e.get("synthesis_path") for e in entries
                    if isinstance(e, dict) and isinstance(e.get("synthesis_path"), str)}
    return {
        "metric_id": "synthesis_coverage",
        "status": "computed" if denominator else "not_computable",
        "numerator": numerator if denominator else None,
        "denominator": denominator if denominator else None,
        "value": 100 * numerator / denominator if denominator else None,
        "unit": "%",
        "scope": "Dossiers non archivés ; synthèse comptée si l'association est unique et les deux fichiers existent.",
        "excluded_count": len(dossiers) - denominator,
        "unknown_count": sum(len(v) for v in issues.values()),
        "issues": issues,
        "active_dossier_ids": sorted(str(d.get("id")) for d in active if d.get("id")),
        "covered_dossier_ids": sorted(covered),
        "uncovered_dossier_ids": sorted(set(uncovered)),
        "excluded_dossier_ids": sorted(str(d.get("id")) for d in dossiers
                                       if isinstance(d, dict) and d.get("status") == "archived" and d.get("id")),
        "unique_synthesis_count": len(unique_paths),
        "definition_version": 1,
    }

def calculate_connectivity_diagnostics(relations, known_ids, node_type_by_id, relation_definitions):
    """Describe observed graph connectivity without prescribing minimum degrees."""
    relation_types = sorted(
        item.get("id") for item in relation_definitions
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    )
    valid_edges, integrity = inspect_relations(
        relations, known_ids, set(relation_types), node_type_by_id, relation_definitions
    )
    nodes_by_type = {}
    for node_id, node_type in node_type_by_id.items():
        nodes_by_type.setdefault(node_type, set()).add(node_id)

    # Keep relation identifiers per node: a self-loop is one incident relation,
    # while a relation joining two nodes of the same type touches that type once.
    incident_by_node = {node_id: set() for node_id in node_type_by_id}
    relation_ids_by_type = {node_type: set() for node_type in nodes_by_type}
    for edge in valid_edges:
        relation_id = edge["id"]
        source, target = edge["from"], edge["to"]
        incident_by_node[source].add(relation_id)
        incident_by_node[target].add(relation_id)
        relation_ids_by_type[node_type_by_id[source]].add(relation_id)
        relation_ids_by_type[node_type_by_id[target]].add(relation_id)

    summaries = {}
    for node_type, identifiers in sorted(nodes_by_type.items()):
        incoming = {kind: 0 for kind in relation_types}
        outgoing = {kind: 0 for kind in relation_types}
        for edge in valid_edges:
            kind = edge.get("type")
            if edge.get("from") in identifiers:
                outgoing[kind] = outgoing.get(kind, 0) + 1
            if edge.get("to") in identifiers:
                incoming[kind] = incoming.get(kind, 0) + 1
        degrees = [len(incident_by_node[node_id]) for node_id in identifiers]
        distribution = {}
        for degree in degrees:
            label = str(degree)
            distribution[label] = distribution.get(label, 0) + 1
        node_count = len(identifiers)
        connected_count = sum(degree > 0 for degree in degrees)
        summaries[node_type] = {
            "node_count": node_count,
            "nodes_with_relations": connected_count,
            "connectivity_rate": connected_count / node_count if node_count else None,
            "degree_min": min(degrees) if degrees else None,
            "degree_mean": sum(degrees) / node_count if node_count else None,
            "degree_max": max(degrees) if degrees else None,
            "degree_distribution": dict(sorted(distribution.items(), key=lambda item: int(item[0]))),
            "relation_type_counts": {
                kind: sum(1 for edge in valid_edges
                          if edge["id"] in relation_ids_by_type[node_type]
                          and edge["type"] == kind)
                for kind in relation_types
                if any(edge["id"] in relation_ids_by_type[node_type] and edge["type"] == kind
                       for edge in valid_edges)
            },
            "isolated_node_ids": sorted(node_id for node_id in identifiers
                                        if not incident_by_node[node_id]),
            "incoming_by_relation_type": {k: v for k, v in incoming.items() if v},
            "outgoing_by_relation_type": {k: v for k, v in outgoing.items() if v},
        }

    by_relation_type = {}
    for edge in valid_edges:
        kind = edge.get("type")
        by_relation_type[kind] = by_relation_type.get(kind, 0) + 1

    return {
        "scope": "Nœuds des registres indexés ; relations structurellement et sémantiquement valides.",
        "node_types": summaries,
        "valid_relation_count_by_type": dict(sorted(by_relation_type.items())),
        "excluded_invalid_relation_count": len(relations) - len(valid_edges),
        "integrity_diagnostics": {k: v for k, v in integrity.items() if v},
        "interpretation": (
            "Descriptif uniquement : aucun degré minimal, statut d'anomalie ou score global "
            "n'est déduit de l'isolement ou du nombre de relations."
        ),
        "definition_version": 1,
    }


def build_report(data):
    known, duplicate_nodes = build_known_ids(data)
    node_type_by_id = build_node_type_index(data)
    relation_types = {r.get("id") for r in data["relation_definitions"] if isinstance(r, dict)}
    source = calculate_source_coverage(
        data["registries"]["sources"], data["relations"], known, relation_types,
        node_type_by_id, data["relation_definitions"]
    )
    if duplicate_nodes:
        source["issues"]["duplicate_node_ids"] = sorted(duplicate_nodes)
        source["unknown_count"] += len(duplicate_nodes)
    synthesis = calculate_synthesis_coverage(
        data["registries"]["dossiers"], data["synthesis_entries"], ROOT
    )
    connectivity = calculate_connectivity_diagnostics(
        data["relations"], known, node_type_by_id, data["relation_definitions"]
    )
    return {
        "definition_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "metrics": [source, calculate_claim_conclusion_coverage(data["registries"]["claims"]), synthesis],
        "diagnostics": {"known_node_count": len(known), "relation_count": len(data["relations"]),
                        "duplicate_node_ids": sorted(duplicate_nodes),
                        "connectivity": connectivity},
    }

def render_markdown(report):
    lines = ["# KPIs de Society Lab", "", f"Instantané : {report['generated_at']}", "",
             "| KPI | Résultat | Numérateur / dénominateur | Statut |",
             "|---|---:|---:|---|"]
    for metric in report["metrics"]:
        value = "non calculable" if metric["value"] is None else f"{metric['value']:.1f} %"
        ratio = "—" if metric["numerator"] is None else f"{metric['numerator']} / {metric['denominator']}"
        lines.append(f"| {metric['metric_id']} | {value} | {ratio} | {metric['status']} |")
    for metric in report["metrics"]:
        lines.extend(["", f"## {metric['metric_id']}"])
        if "uncovered_source_ids" in metric:
            lines.append(f"Sources sans relation retenue ({len(metric['uncovered_source_ids'])}) :")
            lines.extend(f"- {item}" for item in metric["uncovered_source_ids"])
        elif "status_counts" in metric:
            lines.append(f"Claims exclus (superseded) : {metric['excluded_count']}")
            lines.append(f"Statuts : {json.dumps(metric['status_counts'], ensure_ascii=False, sort_keys=True)}")
        else:
            lines.append(f"Dossiers sans synthèse valide ({len(metric['uncovered_dossier_ids'])}) :")
            lines.extend(f"- {item}" for item in metric["uncovered_dossier_ids"])
            lines.append(f"Fichiers de synthèse distincts : {metric['unique_synthesis_count']}")
        lines.append(f"Anomalies : {json.dumps(metric['issues'], ensure_ascii=False, sort_keys=True)}")
    lines.extend(["", f"Relations : {report['diagnostics']['relation_count']} ; "
                  f"nœuds indexés : {report['diagnostics']['known_node_count']}."])
    connectivity = report["diagnostics"].get("connectivity", {})
    lines.extend(["", "## Connectivité descriptive par type de nœud"])
    lines.append(connectivity.get("interpretation", "Diagnostic non disponible."))
    for node_type, summary in sorted(connectivity.get("node_types", {}).items()):
        lines.append(
            f"- **{node_type}** : {summary['nodes_with_relations']}/"
            f"{summary['node_count']} nœuds avec relation "
            f"({summary['connectivity_rate']:.1%}) ; "
            f"degré min/moyen/max : {summary['degree_min']}/"
            f"{summary['degree_mean']:.2f}/{summary['degree_max']} ; "
            f"distribution : {json.dumps(summary['degree_distribution'], ensure_ascii=False, sort_keys=True)} ; "
            f"{len(summary['isolated_node_ids'])} isolés."
        )
        if summary["isolated_node_ids"]:
            lines.extend(f"  - Isolé : {identifier}" for identifier in summary["isolated_node_ids"])
        if summary["incoming_by_relation_type"] or summary["outgoing_by_relation_type"]:
            lines.append(
                "  - Entrantes : " + json.dumps(summary["incoming_by_relation_type"], ensure_ascii=False, sort_keys=True)
                + " ; sortantes : " + json.dumps(summary["outgoing_by_relation_type"], ensure_ascii=False, sort_keys=True)
            )
    lines.append(
        "Relations valides par type : "
        + json.dumps(connectivity.get("valid_relation_count_by_type", {}), ensure_ascii=False, sort_keys=True)
    )
    return "\n".join(lines) + "\n"

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        report = build_report(load_project_data())
        output = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) if args.format == "json" else render_markdown(report)
        if args.output:
            args.output.write_text(output if output.endswith("\n") else output + "\n", encoding="utf-8")
        else:
            sys.stdout.write(output)
        return 0
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: KPI calculation failed: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
