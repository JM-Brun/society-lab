#!/usr/bin/env python3
"""Validate Society Lab registries, JSON schemas, controlled vocabularies and graph edges."""

from pathlib import Path
import re
import sys

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
ID_RE = re.compile(r"^(DOMAIN|TAG|REL|SOURCE|STUDY|DATASET|CLAIM|HYPOTHESIS|DOSSIER|SYNTHESIS|CONCEPT|MECHANISM|ORG|ANALYSIS|METHOD|TERRITORY|FORECAST)-[A-Z0-9][A-Z0-9-]*$")

TAG_GROUPS = {"method", "evidence", "status", "lens", "scale", "horizon"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

REGISTRIES = [
    ("sources/registry.yml", "sources", "SOURCE", "schemas/source.schema.json"),
    ("research/studies/registry.yml", "studies", "STUDY", "schemas/study.schema.json"),
    ("research/datasets/registry.yml", "datasets", "DATASET", "schemas/dataset.schema.json"),
    ("claims/registry.yml", "claims", "CLAIM", "schemas/claim.schema.json"),
    ("hypotheses/registry.yml", "hypotheses", "HYPOTHESIS", "schemas/hypothesis.schema.json"),
    ("forecasts/registry.yml", "forecasts", "FORECAST", "schemas/forecast.schema.json"),
    ("dossiers/registry.yml", "dossiers", "DOSSIER", "schemas/dossier.schema.json"),
    ("knowledge/concepts/registry.yml", "concepts", "CONCEPT", "schemas/concept.schema.json"),
    ("knowledge/mechanisms/registry.yml", "mechanisms", "MECHANISM", "schemas/mechanism.schema.json"),
]


def load_yaml(relative):
    with (ROOT / relative).open(encoding="utf-8") as stream:
        return yaml.safe_load(stream) or {}


def unique_ids(items, label, errors):
    ids = [item.get("id") for item in items]
    if len(ids) != len(set(ids)):
        errors.append(f"Duplicate identifiers in {label}")
    return {value for value in ids if isinstance(value, str)}


def validate_controlled_vocabularies(domains, tags, errors):
    """Validate domain slugs and the controlled tag-group vocabulary."""
    seen_slugs = {}
    for domain in domains:
        domain_id = domain.get("id", "<missing domain id>")
        slug = domain.get("slug")
        if not isinstance(slug, str) or not SLUG_RE.fullmatch(slug):
            errors.append(f"{domain_id}: invalid or missing domain slug {slug!r}")
            continue
        normalized = slug.casefold()
        if normalized in seen_slugs:
            errors.append(
                f"{domain_id}: duplicate domain slug {slug!r}; "
                f"already used by {seen_slugs[normalized]}"
            )
        else:
            seen_slugs[normalized] = domain_id

    for tag in tags:
        tag_id = tag.get("id", "<missing tag id>")
        group = tag.get("group")
        if group not in TAG_GROUPS:
            errors.append(
                f"{tag_id}: unknown or missing tag group {group!r}; "
                f"expected one of {sorted(TAG_GROUPS)}"
            )


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



def validate_territory_hierarchy(territories, errors):
    """Reject self-parenting and cycles in the declared geographic parent tree."""
    parent_by_id = {item.get("id"): item.get("geographic_parent_id")
                    for item in territories if isinstance(item, dict) and isinstance(item.get("id"), str)}
    for territory_id, parent_id in parent_by_id.items():
        if parent_id == territory_id:
            errors.append(f"{territory_id}: territory cannot be its own geographic parent")
    completed = set()
    for start in parent_by_id:
        path = []
        positions = {}
        current = start
        while current in parent_by_id and current not in completed:
            if current in positions:
                cycle = path[positions[current]:] + [current]
                errors.append("Geographic territory parent cycle: " + " -> ".join(cycle))
                break
            positions[current] = len(path)
            path.append(current)
            parent = parent_by_id[current]
            if not isinstance(parent, str) or parent not in parent_by_id:
                break
            current = parent
        completed.update(path)


def validate_relation_definitions(relation_defs, errors):
    """Check reciprocal inverse declarations when both relation types are defined."""
    by_id = {item.get("id"): item for item in relation_defs if isinstance(item, dict) and isinstance(item.get("id"), str)}
    for relation_id, definition in by_id.items():
        inverse_id = definition.get("inverse")
        inverse = by_id.get(inverse_id)
        # Some inverse labels are intentionally reserved but not yet registered.
        if inverse is None:
            continue
        if inverse.get("inverse") != relation_id:
            errors.append(f"{relation_id}: inverse {inverse_id} does not point back to {relation_id}")
        if set(definition.get("from", [])) != set(inverse.get("to", [])):
            errors.append(f"{relation_id}: inverse {inverse_id} has incompatible endpoint types (from/to)")
        if set(definition.get("to", [])) != set(inverse.get("from", [])):
            errors.append(f"{relation_id}: inverse {inverse_id} has incompatible endpoint types (to/from)")

def validate_cross_references(all_records, node_ids, errors):
    """Check both top-level references and nested claim source-verification links."""
    reference_fields = {
        "source_ids": "SOURCE",
        "study_ids": "STUDY",
        "dataset_ids": "DATASET",
        "hypothesis_ids": "HYPOTHESIS",
        "claim_ids": "CLAIM",
        "concept_ids": "CONCEPT",
        "supporting_study_ids": "STUDY",
        "challenging_study_ids": "STUDY",
    }
    for prefix, records in all_records.items():
        for record in records:
            record_id = record.get("id", f"{prefix} record")
            for field, target_type in reference_fields.items():
                for target in record.get(field, []) or []:
                    if target not in node_ids.get(target_type, set()):
                        errors.append(f"{record_id}: unresolved {field} reference {target}")
            for verification in record.get("source_verifications", []) or []:
                target = verification.get("source_id") if isinstance(verification, dict) else None
                if target and target not in node_ids.get("SOURCE", set()):
                    errors.append(f"{record_id}: unresolved source_verifications.source_id reference {target}")


def validate_graph_edges(edges, relation_by_id, node_type_by_id, errors):
    """Validate graph semantics that are not covered by JSON/YAML parsing alone."""
    seen_triples = {}
    for edge in edges:
        edge_id = edge.get("id", "<missing edge id>")
        if not isinstance(edge_id, str) or not ID_RE.fullmatch(edge_id) or not edge_id.startswith("REL-"):
            errors.append(f"Invalid graph edge identifier: {edge_id!r}")

        justification = edge.get("justification")
        if not isinstance(justification, str) or not justification.strip():
            errors.append(f"{edge_id}: missing non-empty relation justification")

        triple = (edge.get("type"), edge.get("from"), edge.get("to"))
        if triple in seen_triples:
            errors.append(
                f"{edge_id}: duplicate relation triple {triple!r}; "
                f"already declared as {seen_triples[triple]}"
            )
        else:
            seen_triples[triple] = edge_id

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



def validate_batch_manifest(batch, label, source_ids, errors):
    """Check batch-local candidate identities and links to canonical sources."""
    candidates = batch.get("candidates", []) or []
    if not isinstance(candidates, list):
        return
    valid_candidates = [candidate for candidate in candidates if isinstance(candidate, dict)]
    candidate_ids = [candidate.get("candidate_id") for candidate in valid_candidates]
    if len(candidate_ids) != len(set(candidate_ids)):
        errors.append(f"{label}: duplicate candidate_id in batch")
    known_candidates = {value for value in candidate_ids if isinstance(value, str)}
    duplicate_links = {}
    selected_sources = set()

    for candidate in valid_candidates:
        candidate_id = candidate.get("candidate_id", "<missing candidate_id>")
        source_id = candidate.get("source_id")
        if source_id and source_id not in source_ids:
            errors.append(f"{label} {candidate_id}: unresolved source_id {source_id}")
        if candidate.get("decision") == "selected" and source_id:
            if source_id in selected_sources:
                errors.append(f"{label}: source_id {source_id} selected more than once in the same batch")
            selected_sources.add(source_id)

        duplicate_of = candidate.get("duplicate_of")
        if duplicate_of:
            if duplicate_of == candidate_id:
                errors.append(f"{label} {candidate_id}: candidate cannot be a duplicate of itself")
            elif duplicate_of not in known_candidates and duplicate_of not in source_ids:
                errors.append(f"{label} {candidate_id}: unresolved duplicate_of {duplicate_of}")
            elif duplicate_of in known_candidates:
                duplicate_links[candidate_id] = duplicate_of

        if batch.get("status") == "closed" and candidate.get("decision") == "deferred":
            errors.append(f"{label} {candidate_id}: closed batch cannot contain deferred candidates")

    for candidate_id in duplicate_links:
        visited = set()
        current = candidate_id
        while current in duplicate_links:
            if current in visited:
                errors.append(f"{label}: duplicate_of cycle involving {candidate_id}")
                break
            visited.add(current)
            current = duplicate_links[current]


def load_batch_validator():
    import json

    schema_path = ROOT / "schemas" / "ingestion-batch.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


def validate_batch_manifests(source_ids, errors):
    """Validate every committed source-ingestion batch manifest, if any exist."""
    directory = ROOT / "sources" / "batches"
    try:
        validator = load_batch_validator()
    except Exception as exc:
        errors.append(f"Invalid schema schemas/ingestion-batch.schema.json: {exc}")
        return

    seen_batch_ids = set()
    for path in sorted([*directory.glob("*.yml"), *directory.glob("*.yaml")]):
        label = path.relative_to(ROOT).as_posix()
        try:
            with path.open(encoding="utf-8") as stream:
                batch = yaml.safe_load(stream) or {}
        except Exception as exc:
            errors.append(f"{label}: invalid YAML: {exc}")
            continue
        if not isinstance(batch, dict):
            errors.append(f"{label}: batch manifest must be a mapping")
            continue
        batch_id = batch.get("batch_id")
        if isinstance(batch_id, str) and batch_id:
            if batch_id in seen_batch_ids:
                errors.append(f"{label}: duplicate batch_id {batch_id}")
            seen_batch_ids.add(batch_id)
        schema_errors = list(validator.iter_errors(batch))
        for error in schema_errors:
            location = ".".join(str(part) for part in error.absolute_path)
            errors.append(f"{label} {location}: {error.message}")
        if not schema_errors:
            validate_batch_manifest(batch, label, source_ids, errors)

def validate_source_event_references(events, node_ids, errors):
    """Validate event identities, source links and review targets."""
    label = "sources/lifecycle.yml"
    known_nodes = set().union(*node_ids.values())
    sources = node_ids.get("SOURCE", set())
    seen_events = set()
    for event in events:
        event_id = event["id"]
        if event_id in seen_events:
            errors.append(f"{label}: duplicate event {event_id}")
        seen_events.add(event_id)
        for field in ("source_id", "replacement_source_id"):
            if field in event and event[field] not in sources:
                errors.append(f"{label} {event_id}: unresolved {field} {event[field]}")
        if event.get("replacement_source_id") == event["source_id"]:
            errors.append(f"{label} {event_id}: replacement_source_id equals source_id")

        seen_targets = set()
        for decision in event["decisions"]:
            target_id = decision["target_id"]
            if target_id not in known_nodes:
                errors.append(f"{label} {event_id}: unresolved target_id {target_id}")
            if target_id in seen_targets:
                errors.append(f"{label} {event_id}: duplicate decision for {target_id}")
            seen_targets.add(target_id)


def main():
    errors = []
    taxonomy = load_yaml("knowledge/TAXONOMY.yml")
    tags_vocab = load_yaml("knowledge/TAGS.yml")
    relation_vocab = load_yaml("knowledge/RELATION_TYPES.yml")
    territories_vocab = load_yaml("knowledge/TERRITORIES.yml")

    domains = unique_ids(taxonomy.get("domains", []), "knowledge/TAXONOMY.yml", errors)
    tags = unique_ids(tags_vocab.get("tags", []), "knowledge/TAGS.yml", errors)
    validate_controlled_vocabularies(taxonomy.get("domains", []), tags_vocab.get("tags", []), errors)
    relation_defs = relation_vocab.get("relations", [])
    territories = territories_vocab.get("territories", [])
    territory_ids = unique_ids(territories, "knowledge/TERRITORIES.yml", errors)
    node_ids = {"DOMAIN": domains, "TAG": tags, "TERRITORY": territory_ids}
    node_type_by_id = {identifier: kind for kind, values in node_ids.items() for identifier in values}
    validate_schema_and_records("schemas/territory.schema.json", territories, "knowledge/TERRITORIES.yml", errors)
    for territory in territories:
        parent_id = territory.get("geographic_parent_id")
        if parent_id and parent_id not in territory_ids:
            errors.append(f"{territory.get('id')}: unknown parent territory {parent_id}")
    relation_types = unique_ids(relation_defs, "knowledge/RELATION_TYPES.yml", errors)
    validate_relation_definitions(relation_defs, errors)
    validate_territory_hierarchy(territories, errors)

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

    validate_cross_references(all_records, node_ids, errors)
    validate_batch_manifests(node_ids.get('SOURCE', set()), errors)

    # Synthesis documents are first-class graph nodes, sourced from the synthesis registry.
    synthesis_registry = load_yaml("syntheses/registry.yml")
    synthesis_ids = {
        entry.get("synthesis_id")
        for entry in synthesis_registry.get("dossiers", [])
        if isinstance(entry, dict) and isinstance(entry.get("synthesis_id"), str)
    }
    for identifier in synthesis_ids:
        if not ID_RE.fullmatch(identifier) or not identifier.startswith("SYNTHESIS-"):
            errors.append(f"Invalid synthesis identifier: {identifier!r}")
    node_ids["SYNTHESIS"] = synthesis_ids
    node_type_by_id.update({identifier: "SYNTHESIS" for identifier in synthesis_ids})

    journal = load_yaml("sources/lifecycle.yml")
    previous_error_count = len(errors)
    validate_schema_and_records(
        "schemas/source-lifecycle.schema.json", [journal], "sources/lifecycle.yml", errors,
    )
    if len(errors) == previous_error_count:
        validate_source_event_references(journal["events"], node_ids, errors)

    graph = load_yaml("knowledge/graph.yml")
    edges = graph.get("relations", [])
    unique_ids(edges, "knowledge/graph.yml", errors)
    relation_by_id = {item["id"]: item for item in relation_defs}
    validate_graph_edges(edges, relation_by_id, node_type_by_id, errors)

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print("Society Lab schemas, records, references and knowledge graph: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
