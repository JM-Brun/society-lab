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
    }

def build_known_ids(data: dict[str, Any]) -> tuple[set[str], list[str]]:
    known, duplicates = set(), []
    groups = list(data["registries"].values()) + [data["domains"], data["territories"]]
    groups.append([{"id": row.get("synthesis_id")} for row in data["synthesis_entries"]])
    for records in groups:
        for record in records:
            if not isinstance(record, dict):
                continue
            identifier = record.get("id")
            if isinstance(identifier, str) and identifier:
                if identifier in known:
                    duplicates.append(identifier)
                known.add(identifier)
    # Several dossier rows intentionally share one synthesis_id; deduplicate this mapping.
    for row in data["synthesis_entries"]:
        identifier = row.get("synthesis_id") if isinstance(row, dict) else None
        if isinstance(identifier, str) and identifier:
            known.add(identifier)
    return known, duplicates

def inspect_relations(relations: list[dict[str, Any]], known_ids: set[str]):
    valid, diagnostics = [], {key: [] for key in (
        "missing_ids", "duplicate_ids", "duplicate_triples", "empty_justifications",
        "unknown_endpoints", "unknown_relation_types")}
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
        if not isinstance(kind, str) or not kind:
            diagnostics["unknown_relation_types"].append(str(edge_id)); invalid = True
        if not invalid:
            valid.append(edge)
    return valid, diagnostics

def calculate_source_coverage(sources, relations, known_ids):
    source_ids = {r["id"] for r in sources if isinstance(r, dict) and isinstance(r.get("id"), str)}
    valid_edges, diagnostics = inspect_relations(relations, known_ids)
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
        "definition_version": 1,
    }


def calculate_synthesis_coverage(dossiers, entries, root: Path):
    """Measure active dossier coverage; shared synthesis files are intentional."""
    active_statuses = {"scoping", "researching", "draft", "under_review", "published"}
    active = [d for d in dossiers if isinstance(d, dict) and d.get("status") != "archived"]
    dossier_ids = {d.get("id") for d in active if isinstance(d.get("id"), str)}
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
        "uncovered_dossier_ids": sorted(set(uncovered)),
        "unique_synthesis_count": len(unique_paths),
        "definition_version": 1,
    }

def build_report(data):
    known, duplicate_nodes = build_known_ids(data)
    source = calculate_source_coverage(data["registries"]["sources"], data["relations"], known)
    if duplicate_nodes:
        source["issues"]["duplicate_node_ids"] = sorted(duplicate_nodes)
        source["unknown_count"] += len(duplicate_nodes)
    synthesis = calculate_synthesis_coverage(
        data["registries"]["dossiers"], data["synthesis_entries"], ROOT
    )
    return {
        "definition_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "metrics": [source, calculate_claim_conclusion_coverage(data["registries"]["claims"]), synthesis],
        "diagnostics": {"known_node_count": len(known), "relation_count": len(data["relations"]),
                        "duplicate_node_ids": sorted(duplicate_nodes)},
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
