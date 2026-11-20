#!/usr/bin/env python3
"""Report differences between explicit registry references and graph edges."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
REGISTRIES = {
    "DOSSIER": ("dossiers/registry.yml", "dossiers"),
    "STUDY": ("research/studies/registry.yml", "studies"),
}
# Only compare fields whose documentary meaning overlaps with the given edge.
RULES = (
    ("DOSSIER", "study_ids", "REL-INCLUDES", "STUDY"),
    ("DOSSIER", "claim_ids", "REL-INCLUDES", "CLAIM"),
    ("DOSSIER", "hypothesis_ids", "REL-INCLUDES", "HYPOTHESIS"),
    ("DOSSIER", "concept_ids", "REL-INCLUDES", "CONCEPT"),
    ("STUDY", "dataset_ids", "REL-USES", "DATASET"),
)
SIDES = {"registry_only": "fiches seules", "graph_only": "graphe seul"}
SUMMARY_LIMIT = 30


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, encoding="utf-8",
    ).stdout


def resolve_revision(ref: str) -> str:
    return git("rev-parse", "--verify", "--end-of-options", f"{ref}^{{commit}}").strip()


def load_snapshot(revision: str) -> tuple[dict, list]:
    registries = {
        kind: yaml.safe_load(git("show", f"{revision}:{path}"))[collection]
        for kind, (path, collection) in REGISTRIES.items()
    }
    edges = yaml.safe_load(git("show", f"{revision}:knowledge/graph.yml"))["relations"]
    return registries, edges


def compare_snapshots(current: tuple[dict, list], baseline: tuple[dict, list] | None = None) -> list[dict]:
    def pairs(snapshot: tuple[dict, list], rule: tuple[str, ...]) -> tuple[set, set]:
        registries, edges = snapshot
        source_type, field, relation, target_type = rule
        declared = {
            (record["id"], target)
            for record in registries[source_type]
            for target in record.get(field, [])
        }
        observed = {
            (edge["from"], edge["to"])
            for edge in edges
            if edge["type"] == relation
            and edge["from"].startswith(f"{source_type}-")
            and edge["to"].startswith(f"{target_type}-")
        }
        return declared, observed

    comparisons = []
    for rule in RULES:
        source_type, field, relation, target_type = rule
        declared, observed = pairs(current, rule)
        gaps = (declared - observed, observed - declared)
        report = {
            "source_type": source_type,
            "field": field,
            "relation": relation,
            "target_type": target_type,
            "matching_count": len(declared & observed),
            **{side: sorted(items) for side, items in zip(SIDES, gaps, strict=True)},
        }
        if baseline is not None:
            before_declared, before_observed = pairs(baseline, rule)
            before = (before_declared - before_observed, before_observed - before_declared)
            report["changes"] = {
                side: {"added": sorted(new - old), "resolved": sorted(old - new)}
                for side, new, old in zip(SIDES, gaps, before, strict=True)
            }
        comparisons.append(report)
    return comparisons


def render_markdown(report: dict) -> str:
    lines = ["## Rapprochement fiches–graphe", "", f"Révision auditée `{report['revision']}`."]
    if report["base_revision"] is not None:
        lines.append(f"Révision de référence `{report['base_revision']}`.")
    lines.extend([
        "", "Les écarts sont des éléments à examiner selon le rôle documentaire de chaque lien.", "",
        "| Fiche et champ | Relation | Communes | Fiches seules | Graphe seul |",
        "|---|---|---:|---:|---:|",
    ])
    details = []
    added = resolved = 0
    for rule in report["rules"]:
        field = f"`{rule['source_type']}.{rule['field']}`"
        lines.append(
            f"| {field} | `{rule['relation']}` | {rule['matching_count']} | "
            f"{len(rule['registry_only'])} | {len(rule['graph_only'])} |"
        )
        for side, changes in rule.get("changes", {}).items():
            added += len(changes["added"])
            resolved += len(changes["resolved"])
            for change, label in (("added", "Apparu"), ("resolved", "Disparu")):
                remaining = SUMMARY_LIMIT - len(details)
                details.extend(
                    f"- {label} ({SIDES[side]}, {field}) · `{source}` → `{target}`"
                    for source, target in changes[change][:remaining]
                )
    if report["base_revision"] is not None:
        lines.extend(["", "### Évolution des écarts", "", f"**Apparus** {added} · **Disparus** {resolved}"])
        if details:
            lines.extend(["", *details])
        if added + resolved > SUMMARY_LIMIT:
            lines.extend(["", f"Les {SUMMARY_LIMIT} premiers changements sont affichés. Le rapport JSON contient la liste complète."])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="HEAD", help="Git commit or ref to audit (default: HEAD)")
    parser.add_argument("--base", help="Git commit or ref to compare against")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--json-output", type=Path, help="Also write the full JSON report to this path")
    args = parser.parse_args()

    try:
        revision = resolve_revision(args.revision)
        base = resolve_revision(args.base) if args.base else None
        report = {
            "revision": revision,
            "base_revision": base,
            "rules": compare_snapshots(load_snapshot(revision), load_snapshot(base) if base else None),
        }
    except subprocess.CalledProcessError as exc:
        parser.error(exc.stderr.strip() or "unable to read the requested Git revisions")
    except (KeyError, TypeError, yaml.YAMLError) as exc:
        parser.error(f"invalid registry or graph snapshot: {exc}")

    serialized = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    if args.json_output:
        args.json_output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized if args.format == "json" else render_markdown(report))


if __name__ == "__main__":
    main()
