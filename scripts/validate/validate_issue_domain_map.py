#!/usr/bin/env python3
"""Validate explicit GitHub issue to canonical dossier/domain mappings."""
from __future__ import annotations

import sys
from pathlib import Path

import yaml


def validate_mapping(mapping: dict, dossier_registry: dict, taxonomy: dict) -> list[str]:
    errors = []
    dossier_entries = dossier_registry.get("dossiers", [])
    dossier_ids = {item["id"] for item in dossier_entries}
    domain_ids = {item["id"] for item in taxonomy.get("domains", [])}
    entries = mapping.get("issues", [])
    numbers = [item.get("issue") for item in entries]
    if len(numbers) != len(set(numbers)):
        errors.append("issue numbers must be unique")
    known_issues = set(numbers)
    for item in entries:
        number = item.get("issue")
        kind = item.get("kind")
        if not isinstance(number, int) or number < 1:
            errors.append(f"invalid issue number: {number!r}")
        if kind not in {"research", "meta", "technical", "documentation"}:
            errors.append(f"issue #{number}: unsupported kind {kind!r}")
        linked = item.get("dossier_ids", [])
        if kind == "meta" and linked:
            errors.append(f"issue #{number}: meta issue must not invent a dossier association")
        if kind == "research" and not linked:
            errors.append(f"issue #{number}: research issue requires an explicit dossier")
        for dossier_id in linked:
            if dossier_id not in dossier_ids:
                errors.append(f"issue #{number}: unknown dossier {dossier_id}")
        for dependency in item.get("depends_on", []):
            if dependency not in known_issues:
                errors.append(f"issue #{number}: dependency #{dependency} has no explicit mapping")
            if dependency == number:
                errors.append(f"issue #{number}: self-dependency is invalid")
    for dossier in dossier_entries:
        for domain_id in dossier.get("domain_ids", []):
            if domain_id not in domain_ids:
                errors.append(f"dossier {dossier['id']}: unknown domain {domain_id}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    with (root / "governance/issue-domain-map.yml").open(encoding="utf-8") as stream:
        mapping = yaml.safe_load(stream)
    with (root / "dossiers/registry.yml").open(encoding="utf-8") as stream:
        dossiers = yaml.safe_load(stream)
    with (root / "knowledge/TAXONOMY.yml").open(encoding="utf-8") as stream:
        taxonomy = yaml.safe_load(stream)
    errors = validate_mapping(mapping, dossiers, taxonomy)
    if errors:
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Validated {len(mapping.get('issues', []))} explicit issue mappings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
