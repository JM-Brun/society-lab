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
EXCEPTIONS_PATH = "governance/graph-reconciliation-exceptions.yml"


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


def load_exceptions(revision: str) -> list[dict]:
    if not git("ls-tree", "--name-only", revision, "--", EXCEPTIONS_PATH).strip():
        return []
    exceptions = yaml.safe_load(git("show", f"{revision}:{EXCEPTIONS_PATH}"))["exceptions"]
    if not isinstance(exceptions, list):
        raise ValueError("reconciliation exceptions must be a list")
    return exceptions


def classify_exceptions(rules: list[dict], exceptions: list[dict]) -> dict:
    gaps = {
        (rule["field"], side, source, target)
        for rule in rules
        for side in SIDES
        for source, target in rule[side]
    }
    endpoints = {field: (source_type, target_type) for source_type, field, _, target_type in RULES}
    active, inactive = [], []
    seen = set()
    keys = ("field", "side", "source", "target", "reason")
    for i, entry in enumerate(exceptions, start=1):
        if not isinstance(entry, dict) or set(entry) != set(keys) or any(
            not isinstance(entry[key], str) or not entry[key].strip() for key in keys
        ):
            raise ValueError(f"invalid reconciliation exception #{i}")
        key = tuple(entry[k] for k in keys[:-1])
        field, side, source, target = key
        if field not in endpoints or side not in SIDES:
            raise ValueError(f"unknown field or side in reconciliation exception #{i}")
        source_type, target_type = endpoints[field]
        if not source.startswith(f"{source_type}-") or not target.startswith(f"{target_type}-"):
            raise ValueError(f"invalid endpoints in reconciliation exception #{i}")
        if key in seen:
            raise ValueError(f"duplicate reconciliation exception #{i}: {key}")
        seen.add(key)
        (active if key in gaps else inactive).append(entry)
    order = lambda entry: tuple(entry[k] for k in keys[:-1])
    return {
        "unreviewed_count": len(gaps) - len(active),
        "documented_exceptions": sorted(active, key=order),
        "inactive_exceptions": sorted(inactive, key=order),
    }


def render_markdown(report: dict) -> str:
    lines = ["## Rapprochement fiches–graphe", "", f"Révision auditée `{report['revision']}`."]
    if report["base_revision"] is not None:
        lines.append(f"Révision de référence `{report['base_revision']}`.")
    lines.extend([
        "", "Le tableau conserve les écarts bruts entre les fiches et le graphe.", "",
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
    if "unreviewed_count" in report:
        documented = report["documented_exceptions"]
        inactive = report["inactive_exceptions"]
        lines.extend([
            "",
            f"**À examiner** {report['unreviewed_count']} · **Écarts documentés** {len(documented)}"
            f" · **Décisions sans écart correspondant** {len(inactive)}",
        ])
        for label, entries in (("Écarts documentés", documented), ("Décisions à réexaminer", inactive)):
            if entries:
                lines.extend(["", f"### {label}", ""])
                lines.extend(
                    f"- `{entry['source']}` → `{entry['target']}` "
                    f"(`{entry['field']}`, {SIDES[entry['side']]}). {entry['reason']}"
                    for entry in entries
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
        report.update(classify_exceptions(report["rules"], load_exceptions(revision)))
    except subprocess.CalledProcessError as exc:
        parser.error(exc.stderr.strip() or "unable to read the requested Git revisions")
    except (KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        parser.error(f"invalid registry, graph, or exception data: {exc}")

    serialized = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    if args.json_output:
        args.json_output.write_text(serialized + "\n", encoding="utf-8")
    print(serialized if args.format == "json" else render_markdown(report))


if __name__ == "__main__":
    main()
