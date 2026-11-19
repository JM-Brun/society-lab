#!/usr/bin/env python3
"""Benchmark the registry/schema/reference/graph validator on scaled synthetic corpora.

This measures validation work in-process. It deliberately does not claim to measure
site generation, external API calls, or scientific review.
"""
from __future__ import annotations

import argparse
import copy
import gc
import json
import sys
import time
import tracemalloc
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "validate"))

from validate_registry import (  # noqa: E402
    REGISTRIES,
    load_yaml,
    unique_ids,
    validate_batch_manifests,
    validate_controlled_vocabularies,
    validate_cross_references,
    validate_graph_edges,
    validate_relation_definitions,
    validate_schema_and_records,
    validate_territory_hierarchy,
)


def remap(value, mapping):
    if isinstance(value, dict):
        return {key: remap(item, mapping) for key, item in value.items()}
    if isinstance(value, list):
        return [remap(item, mapping) for item in value]
    if isinstance(value, str):
        return mapping.get(value, value)
    return value


def load_base():
    started = time.perf_counter()
    taxonomy = load_yaml("knowledge/TAXONOMY.yml")
    tags_vocab = load_yaml("knowledge/TAGS.yml")
    relations_vocab = load_yaml("knowledge/RELATION_TYPES.yml")
    territories_vocab = load_yaml("knowledge/TERRITORIES.yml")
    base_records = {
        prefix: load_yaml(relative).get(collection, [])
        for relative, collection, prefix, _schema in REGISTRIES
    }
    graph_edges = load_yaml("knowledge/graph.yml").get("relations", [])
    synthesis_registry = load_yaml("syntheses/registry.yml")
    synthesis_ids = {
        entry.get("synthesis_id")
        for entry in synthesis_registry.get("dossiers", [])
        if isinstance(entry, dict) and isinstance(entry.get("synthesis_id"), str)
    }
    elapsed_ms = (time.perf_counter() - started) * 1000
    return {
        "taxonomy": taxonomy,
        "tags": tags_vocab,
        "relations": relations_vocab.get("relations", []),
        "territories": territories_vocab.get("territories", []),
        "records": base_records,
        "edges": graph_edges,
        "synthesis_ids": synthesis_ids,
        "load_ms": elapsed_ms,
    }


def scale_corpus(base, factor):
    records = {kind: copy.deepcopy(items) for kind, items in base["records"].items()}
    edges = copy.deepcopy(base["edges"])
    synthesis_ids = set(base["synthesis_ids"])
    all_node_ids = {
        record["id"]
        for items in base["records"].values()
        for record in items
        if isinstance(record.get("id"), str)
    } | synthesis_ids
    all_edge_ids = {
        edge["id"] for edge in base["edges"] if isinstance(edge.get("id"), str)
    }
    static_node_ids = {
        item["id"]
        for collection in (
            base["taxonomy"].get("domains", []),
            base["tags"].get("tags", []),
            base["territories"],
        )
        for item in collection
        if isinstance(item.get("id"), str)
    }

    for replicate in range(1, factor):
        mapping = {
            identifier: f"{identifier}-SCALE-{replicate}"
            for identifier in all_node_ids | all_edge_ids
        }
        for kind, items in base["records"].items():
            records[kind].extend(remap(item, mapping) for item in items)
        synthesis_ids.update(mapping[item] for item in base["synthesis_ids"])
        # Purely static territory-to-territory edges are not cloned: doing so
        # would create duplicate triples rather than scale record-linked edges.
        for edge in base["edges"]:
            if edge.get("from") in static_node_ids and edge.get("to") in static_node_ids:
                continue
            edges.append(remap(edge, mapping))

    return records, edges, synthesis_ids


def run_validation(base, factor):
    build_started = time.perf_counter()
    records, edges, synthesis_ids = scale_corpus(base, factor)
    build_ms = (time.perf_counter() - build_started) * 1000
    validation_started = time.perf_counter()
    errors = []
    domains = base["taxonomy"].get("domains", [])
    tags = base["tags"].get("tags", [])
    territories = base["territories"]
    relation_defs = base["relations"]

    domain_ids = unique_ids(domains, "knowledge/TAXONOMY.yml", errors)
    tag_ids = unique_ids(tags, "knowledge/TAGS.yml", errors)
    territory_ids = unique_ids(territories, "knowledge/TERRITORIES.yml", errors)
    validate_controlled_vocabularies(domains, tags, errors)
    validate_relation_definitions(relation_defs, errors)
    validate_territory_hierarchy(territories, errors)

    node_ids = {"DOMAIN": domain_ids, "TAG": tag_ids, "TERRITORY": territory_ids}
    node_type_by_id = {
        identifier: kind
        for kind, identifiers in node_ids.items()
        for identifier in identifiers
    }
    for relative, _collection, prefix, schema_path in REGISTRIES:
        items = records[prefix]
        identifiers = unique_ids(items, relative, errors)
        node_ids[prefix] = identifiers
        node_type_by_id.update({identifier: prefix for identifier in identifiers})
        validate_schema_and_records(schema_path, items, relative, errors)

    node_ids["SYNTHESIS"] = synthesis_ids
    node_type_by_id.update({identifier: "SYNTHESIS" for identifier in synthesis_ids})
    validate_cross_references(records, node_ids, errors)
    validate_batch_manifests(node_ids["SOURCE"], errors)
    unique_ids(edges, "knowledge/graph.yml", errors)
    relation_by_id = {item["id"]: item for item in relation_defs}
    validate_graph_edges(edges, relation_by_id, node_type_by_id, errors)
    if errors:
        raise RuntimeError("\n".join(errors[:20]))

    validation_ms = (time.perf_counter() - validation_started) * 1000
    return {
        "scale": factor,
        "records": sum(len(items) for items in records.values()),
        "edges": len(edges),
        "build_ms": round(build_ms, 2),
        "validation_ms": round(validation_ms, 2),
    }


def benchmark(scales):
    base = load_base()
    results = []
    for factor in scales:
        gc.collect()
        tracemalloc.start()
        started = time.perf_counter()
        counts = run_validation(base, factor)
        total_ms = (time.perf_counter() - started) * 1000
        _current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        results.append({
            **counts,
            "total_ms": round(total_ms, 2),
            "peak_memory_mb": round(peak / (1024 * 1024), 2),
        })
    return {"base_yaml_load_ms": round(base["load_ms"], 2), "results": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scales", nargs="+", type=int, default=[1, 10, 100])
    args = parser.parse_args()
    if any(scale < 1 for scale in args.scales):
        parser.error("scales must be positive integers")
    print(json.dumps(benchmark(args.scales), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
