#!/usr/bin/env python3
"""Validate Society Lab's YAML registries and semantic identifiers."""

from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
ID_PATTERN = re.compile(r"^(DOMAIN|SOURCE|CLAIM)-[A-Z0-9][A-Z0-9-]*$")


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def main() -> int:
    errors: list[str] = []
    taxonomy = load_yaml(ROOT / "knowledge/TAXONOMY.yml")
    domains = taxonomy.get("domains", [])
    domain_ids = [item.get("id") for item in domains]

    if len(domain_ids) != len(set(domain_ids)):
        errors.append("Duplicate domain identifiers in knowledge/TAXONOMY.yml")

    for identifier in domain_ids:
        if not isinstance(identifier, str) or not ID_PATTERN.fullmatch(identifier):
            errors.append(f"Invalid domain identifier: {identifier!r}")

    for relative, collection_key, prefix in [
        ("sources/registry.yml", "sources", "SOURCE-"),
        ("claims/registry.yml", "claims", "CLAIM-"),
    ]:
        payload = load_yaml(ROOT / relative)
        records = payload.get(collection_key, [])
        identifiers = [record.get("id") for record in records]

        if len(identifiers) != len(set(identifiers)):
            errors.append(f"Duplicate identifiers in {relative}")

        for identifier in identifiers:
            if not isinstance(identifier, str) or not identifier.startswith(prefix):
                errors.append(f"Invalid identifier in {relative}: {identifier!r}")

        if prefix == "CLAIM-":
            for record in records:
                for domain_id in record.get("domain_ids", []):
                    if domain_id not in domain_ids:
                        errors.append(f"{record.get('id')}: unknown domain {domain_id}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1

    print("Society Lab registries: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
