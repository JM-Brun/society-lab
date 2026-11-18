#!/usr/bin/env python3
"""Informational, read-only benchmark for the project KPI calculator.

Measures YAML loading separately from the three KPI calculations. Synthetic
scales preserve record shapes and valid graph endpoints while assigning unique
identifiers. No repository files are modified.
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "validate"))
from calculate_project_kpis import (  # noqa: E402
    build_known_ids,
    calculate_claim_conclusion_coverage,
    calculate_source_coverage,
    calculate_synthesis_coverage,
    load_project_data,
)


def scaled_snapshot(base, multiplier):
    if multiplier == 1:
        return base
    registries = {}
    id_map = {}
    for key, records in base["registries"].items():
        expanded = []
        for copy_index in range(multiplier):
            for record in records:
                if not isinstance(record, dict):
                    expanded.append(record)
                    continue
                clone = dict(record)
                identifier = record.get("id")
                if isinstance(identifier, str):
                    new_id = f"{identifier}__BENCH_{copy_index}"
                    id_map[(copy_index, identifier)] = new_id
                    clone["id"] = new_id
                expanded.append(clone)
        registries[key] = expanded

    domains, territories = [], []
    for key, target in (("domains", domains), ("territories", territories)):
        for copy_index in range(multiplier):
            for record in base[key]:
                clone = dict(record)
                identifier = record.get("id")
                if isinstance(identifier, str):
                    new_id = f"{identifier}__BENCH_{copy_index}"
                    id_map[(copy_index, identifier)] = new_id
                    clone["id"] = new_id
                target.append(clone)

    relations = []
    for copy_index in range(multiplier):
        for edge in base["relations"]:
            clone = dict(edge)
            clone["id"] = f"{edge.get('id')}__BENCH_{copy_index}"
            for endpoint in ("from", "to"):
                original = edge.get(endpoint)
                clone[endpoint] = id_map.get((copy_index, original), original)
            relations.append(clone)

    claims = registries["claims"]
    dossiers = registries["dossiers"]
    synthesis_entries = []
    for copy_index in range(multiplier):
        for entry in base["synthesis_entries"]:
            clone = dict(entry)
            dossier_id = entry.get("dossier_id")
            clone["dossier_id"] = f"{dossier_id}__BENCH_{copy_index}"
            synthesis_entries.append(clone)

    return {
        "registries": registries,
        "domains": domains,
        "territories": territories,
        "relations": relations,
        "relation_definitions": base["relation_definitions"],
        "synthesis_entries": synthesis_entries,
    }


def calculate(snapshot):
    known, duplicates = build_known_ids(snapshot)
    relation_types = {
        item.get("id") for item in snapshot["relation_definitions"]
        if isinstance(item, dict)
    }
    source = calculate_source_coverage(
        snapshot["registries"]["sources"], snapshot["relations"],
        known, relation_types,
    )
    claims = calculate_claim_conclusion_coverage(snapshot["registries"]["claims"])
    syntheses = calculate_synthesis_coverage(
        snapshot["registries"]["dossiers"], snapshot["synthesis_entries"], ROOT
    )
    return source, claims, syntheses, duplicates


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--scales", type=int, nargs="+", default=[1, 10, 100])
    args = parser.parse_args()
    if args.repeats < 1 or any(scale < 1 for scale in args.scales):
        parser.error("repeats and scales must be positive integers")

    base = load_project_data()
    results = []
    for scale in args.scales:
        snapshot = scaled_snapshot(base, scale)
        # Warm-up outside timed samples.
        calculated = calculate(snapshot)
        if calculated[3]:
            raise SystemExit(f"Duplicate node IDs in synthetic x{scale} snapshot")
        parse_samples, calculate_samples = [], []
        for _ in range(args.repeats):
            started = time.perf_counter()
            load_project_data()
            parse_samples.append(time.perf_counter() - started)
            started = time.perf_counter()
            source, claims, syntheses, duplicates = calculate(snapshot)
            calculate_samples.append(time.perf_counter() - started)
            if duplicates or any(metric["unknown_count"] for metric in (source, claims, syntheses)):
                raise SystemExit(f"Unexpected diagnostics in synthetic x{scale} snapshot")
        results.append({
            "scale": scale,
            "sources": len(snapshot["registries"]["sources"]),
            "claims": len(snapshot["registries"]["claims"]),
            "dossiers": len(snapshot["registries"]["dossiers"]),
            "relations": len(snapshot["relations"]),
            "yaml_load_median_seconds": round(statistics.median(parse_samples), 6),
            "calculation_median_seconds": round(statistics.median(calculate_samples), 6),
            "total_median_seconds": round(statistics.median(parse_samples) + statistics.median(calculate_samples), 6),
        })

    print(json.dumps({
        "benchmark": "society_lab_project_kpis",
        "python": sys.version.split()[0],
        "platform": sys.platform,
        "repeats": args.repeats,
        "results": results,
        "scope": "YAML load and KPI calculations measured separately; synthetic x10/x100 snapshots preserve record shapes and valid graph endpoints; excludes GitHub Actions setup and other validators.",
        "note": "Informational benchmark only; timings vary by runner and are not CI thresholds.",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
