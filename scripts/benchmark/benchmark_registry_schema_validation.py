#!/usr/bin/env python3
"""Reproducible, non-gating benchmark of registry JSON-Schema validation.

This deliberately benchmarks the validator's schema-validation hot path rather
than claiming to time the complete GitHub Actions workflow. It repeats the
repository's real, currently valid records in memory; it does not write files.
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
import validate_registry as registry_validator  # noqa: E402


def load_registry_records():
    records_by_registry = []
    for relative, collection, _prefix, _schema in registry_validator.REGISTRIES:
        document = registry_validator.load_yaml(relative)
        records = document.get(collection, [])
        if not isinstance(records, list):
            raise SystemExit(f"{relative}: expected a list at key {collection!r}")
        records_by_registry.append((relative, _schema, records))
    return records_by_registry


def run_once(registries, multiplier):
    errors = []
    record_count = 0
    started = time.perf_counter()
    for relative, schema_path, records in registries:
        expanded = records * multiplier
        record_count += len(expanded)
        registry_validator.validate_schema_and_records(
            schema_path, expanded, relative, errors
        )
    elapsed = time.perf_counter() - started
    if errors:
        preview = "\n".join(errors[:20])
        raise SystemExit(
            f"Schema validation produced {len(errors)} error(s) at x{multiplier}:\n{preview}"
        )
    return elapsed, record_count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--scales", type=int, nargs="+", default=[1, 10, 100])
    args = parser.parse_args()
    if args.repeats < 1 or any(scale < 1 for scale in args.scales):
        parser.error("repeats and scales must be positive integers")

    registries = load_registry_records()
    baseline_count = sum(len(records) for _, _, records in registries)
    if baseline_count == 0:
        raise SystemExit("No registry records found; refusing to report an empty benchmark.")

    results = []
    for scale in args.scales:
        run_once(registries, scale)  # warm-up
        samples = [run_once(registries, scale)[0] for _ in range(args.repeats)]
        results.append({
            "scale": scale,
            "records": baseline_count * scale,
            "median_seconds": round(statistics.median(samples), 6),
            "samples_seconds": [round(value, 6) for value in samples],
        })

    print(json.dumps({
        "benchmark": "registry_json_schema_validation",
        "python": sys.version.split()[0],
        "platform": sys.platform,
        "registries": len(registries),
        "baseline_records": baseline_count,
        "repeats": args.repeats,
        "results": results,
        "scope": "validate_schema_and_records only; excludes YAML parsing, cross-references, graph validation, issue audit and CI setup",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
