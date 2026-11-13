#!/usr/bin/env python3
"""Validate Society Lab registries, JSON schemas, controlled vocabularies and graph edges."""

from pathlib import Path
import re
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
ID_RE = re.compile(r"^(DOMAIN|TAG|REL|SOURCE|STUDY|DATASET|CLAIM|HYPOTHESIS|DOSSIER|CONCEPT|MECHANISM|ORG|ANALYSIS|METHOD|TERRITORY)-[A-Z0-9][A-Z0-9-]*$")

REGISTRIES = [
    ("sources/registry.yml", "sources", "SOURCE", "schemas/source.schema.json"),
    ("research/studies/registry.yml", "studies", "STUDY", "schemas/study.schema.json"),
    ("research/datasets/registry.yml", "datasets", "DATASET", "schemas/dataset.schema.json"),
    ("claims/registry.yml", "claims", "CLAIM", "schemas/claim.schema.json"),
    ("hypotheses/registry.yml", "hypotheses", "HYPOTHESIS", "schemas/hypothesis.schema.json"),
    ("dossiers/registry.yml", "dossiers", "DOSSIER", "schemas/dossier.schema.json"),
]


def load_yaml(relative):
    with (ROOT / relative).open(encoding="utf-8") as stream:
        return yaml.safe_load(stream) or {}


def unique_ids(items, label, errors):
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        errors.append(f"Duplicate identifiers in {label}")
    return {value for value in ids if isinstance(value, str)}


def validate_schema_and_records(relative, records, label, errors):
    import json
    schema_path = ROOT / relative
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
        for index, record in enumerate(records):
            for error in validator.iter_errors(record):
                location = ".".join(str(part) for part in error.absolute_path)
                errors.append(f"{label}[{index}] {location}: {error.message}")
    except Exception as exc:
        errors.append(f"Invalid schema {relative}: {exc}")


def main():
    errors = []
    taxonomy = load_yaml("knowledge/TAXONOMY.yml")
    tags_vocab = load_yaml("knowledge/TAGS.yml")
    relation_vocab = load_yaml("knowledge/RELATION_TYPES.yml")
    territories_vocab = load_yaml("knowledge/TERRITORIES.yml")

    domains = unique_ids(taxonomy.get("domains", []), "knowledge/TAXONOMY.yml", errors)
    tags = unique_ids(tags_vocab.get("tags", []), "knowledge/TAGS.yml", errors)
    relation_defs = relation_vocab.get("relations", [])
    territories = territories_vocab.get("territories", [])
    territory_ids = unique_ids(territories, "knowledge/TERRITORIES.yml", errors)
    node_ids = {"DOMAIN": domains, "TAG": tags, "TERRITORY": territory_ids}
    node_type_by_id = {identifier: kind for kind, values in node_ids.items() for identifier in values}
    validate_schema_and_records("schemas/territory.schema.json", territories, "knowledge/TERRITORIES.yml", errors)
    for territory in territories:
        parent_id = territory.get("parent_id")
        if parent_id and parent_id not in territory_ids:
            errors.append(f"{territory.get('id')}: unknown parent territory {parent_id}")
    relation_types = unique_ids(relation_defs, "knowledge/RELATION_TYPES.yml", errors)

    for identifier in domains | tags | relation_types | territory_ids:
        if not ID_RE.fullmatch(identifier):
            errors.append(f"Invalid controlled identifier: {identifier}")

    all_records = {}
    for relative, collection, prefix, schema_path in REGISTRIES:
        records = load_yaml(relative).get(collection, [])
        ids = unique_ids(records, relative, errors)
        node_ids[prefix] = ids
        for identifier in ids:
            if not identifier.startswith(prefix + "-") or not ID_RE.fullmatch(identifier):
                errors.append(f"Invalid identifier in {relative}: {identifier!r}")
            node_type_by_id[identifier] = prefix
        validate_schema_and_records(schema_path, records, relative, errors)
        all_records[prefix] = records
        for record in records:
            for field in ("domains", "domain_ids"):
                for domain_id in record.get(field, []) or []:
                    if domain_id not in domains:
                        errors.append(f"{record.get('id')}: unknown domain {domain_id}")
            for tag_id in record.get("tags", []) or []:
                if tag_id not in tags:
                    errors.append(f"{record.get('id')}: unknown tag {tag_id}")

    # Cross-reference checks for the typed links embedded in records.
    reference_fields = {
        "source_ids": "SOURCE", "study_ids": "STUDY", "dataset_ids": "DATASET",
        "hypothesis_ids": "HYPOTHESIS", "claim_ids": "CLAIM",
        "supporting_study_ids": "STUDY", "challenging_study_ids": "STUDY",
    }
    for prefix, records in all_records.items():
        for record in records:
            for field, target_type in reference_fields.items():
                for target in record.get(field, []) or []:
                    if target not in node_ids.get(target_type, set()):
                        errors.append(f"{record.get('id')}: unresolved {field} reference {target}")

    # Check graph edge identifiers, endpoint existence, relation type and endpoint types.
    graph = load_yaml("knowledge/graph.yml")
    edges = graph.get("relations", [])
    unique_ids(edges, "knowledge/graph.yml", errors)
    relation_by_id = {item["id"]: item for item in relation_defs}
    for edge in edges:
        edge_id = edge.get("id")
        if not isinstance(edge_id, str) or not ID_RE.fullmatch(edge_id) or not edge_id.startswith("REL-"):
            errors.append(f"Invalid graph edge identifier: {edge_id!r}")
        definition = relation_by_id.get(edge.get("type"))
        if definition is None:
            errors.append(f"{edge_id}: unknown relation type {edge.get('type')!r}")
            continue
        for endpoint in ("from", "to"):
            target = edge.get(endpoint)
            actual_type = node_type_by_id.get(target)
            allowed = definition.get(endpoint, [])
            if actual_type is None:
                errors.append(f"{edge_id}: unresolved {endpoint} node {target!r}")
            elif actual_type not in allowed:
                errors.append(f"{edge_id}: {endpoint} type {actual_type} not allowed for {edge.get('type')}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("Society Lab schemas, records, references and knowledge graph: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
