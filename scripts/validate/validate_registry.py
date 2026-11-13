#!/usr/bin/env python3
"""Validate Society Lab registries, controlled vocabularies and graph references."""

from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
ID_RE = re.compile(r"^(DOMAIN|TAG|REL|SOURCE|STUDY|DATASET|CLAIM|HYPOTHESIS|DOSSIER|CONCEPT|MECHANISM|ORG|ANALYSIS|METHOD)-[A-Z0-9][A-Z0-9-]*$")

REGISTRIES = [
    ("sources/registry.yml", "sources", "SOURCE"),
    ("research/studies/registry.yml", "studies", "STUDY"),
    ("research/datasets/registry.yml", "datasets", "DATASET"),
    ("claims/registry.yml", "claims", "CLAIM"),
    ("hypotheses/registry.yml", "hypotheses", "HYPOTHESIS"),
    ("dossiers/registry.yml", "dossiers", "DOSSIER"),
]


def load_yaml(relative: str):
    path = ROOT / relative
    with path.open(encoding="utf-8") as stream:
        return yaml.safe_load(stream) or {}


def unique_ids(items, label, errors):
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        errors.append(f"Duplicate identifiers in {label}")
    return {value for value in ids if isinstance(value, str)}


def main() -> int:
    errors = []
    taxonomy = load_yaml("knowledge/TAXONOMY.yml")
    tags = load_yaml("knowledge/TAGS.yml")
    relations_vocab = load_yaml("knowledge/RELATION_TYPES.yml")

    domains = unique_ids(taxonomy.get("domains", []), "knowledge/TAXONOMY.yml", errors)
    tag_ids = unique_ids(tags.get("tags", []), "knowledge/TAGS.yml", errors)
    relation_types = unique_ids(relations_vocab.get("relations", []), "knowledge/RELATION_TYPES.yml", errors)

    for identifier in domains | tag_ids | relation_types:
        if not ID_RE.fullmatch(identifier):
            errors.append(f"Invalid controlled identifier: {identifier}")

    known = set(domains) | set(tag_ids)
    records_by_type = {}
    for relative, collection, prefix in REGISTRIES:
        payload = load_yaml(relative)
        records = payload.get(collection, [])
        ids = unique_ids(records, relative, errors)
        records_by_type[prefix] = ids
        for identifier in ids:
            if not identifier.startswith(prefix + "-") or not ID_RE.fullmatch(identifier):
                errors.append(f"Invalid identifier in {relative}: {identifier!r}")
        for record in records:
            for field in ("domains", "domain_ids"):
                for domain_id in record.get(field, []) or []:
                    if domain_id not in domains:
                        errors.append(f"{record.get('id')}: unknown domain {domain_id}")
            for tag_id in record.get("tags", []) or []:
                if tag_id not in tag_ids:
                    errors.append(f"{record.get('id')}: unknown tag {tag_id}")

    # Graph relations are checked against the declared vocabulary and known registry nodes.
    graph = load_yaml("knowledge/graph.yml")
    graph_ids = unique_ids(graph.get("relations", []), "knowledge/graph.yml", errors)
    known_node_ids = set().union(*records_by_type.values(), domains, tag_ids)
    for relation in graph.get("relations", []) or []:
        rid = relation.get("id")
        if not isinstance(rid, str) or not rid.startswith("REL-"):
            errors.append(f"Invalid graph relation identifier: {rid!r}")
        if relation.get("type") not in relation_types:
            errors.append(f"{rid}: unknown relation type {relation.get('type')!r}")
        for endpoint in ("from", "to"):
            target = relation.get(endpoint)
            if target not in known_node_ids:
                errors.append(f"{rid}: unresolved {endpoint} node {target!r}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("Society Lab vocabularies, registries and graph: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
