#!/usr/bin/env python3
"""Inventory geographic_scope labels and exact vocabulary matches at a Git revision."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import defaultdict

import yaml

from audit_registry_coverage import TARGETS
from report_graph_reconciliation import git, resolve_revision


SCOPE_PREFIXES = {"SOURCE", "STUDY", "DATASET", "DOSSIER"}


def geographic_inventory(registries: dict[str, list[dict]], territories: list[dict]) -> dict:
    territory_ids = defaultdict(set)
    for territory in territories:
        territory_ids[territory["label"]].add(territory["id"])

    occurrences = defaultdict(list)
    counts = {}
    for registry, records in sorted(registries.items()):
        populated = values = 0
        for record in records:
            labels = record.get("geographic_scope", [])
            if not isinstance(labels, list) or any(
                not isinstance(label, str) or not label.strip() for label in labels
            ):
                raise ValueError(f"{registry}: invalid geographic_scope on {record['id']}")
            populated += bool(labels)
            values += len(labels)
            for label in labels:
                occurrences[label].append(record["id"])
        counts[registry] = {"records": len(records), "populated": populated, "values": values}

    labels = [
        {
            "label": label,
            "count": len(record_ids),
            "record_ids": sorted(set(record_ids)),
            "exact_territory_ids": sorted(territory_ids.get(label, ())),
        }
        for label, record_ids in sorted(occurrences.items())
    ]
    return {
        "registries": counts,
        "distinct_labels": len(labels),
        "labels_with_exact_match": sum(bool(row["exact_territory_ids"]) for row in labels),
        "labels_with_multiple_exact_matches": sum(len(row["exact_territory_ids"]) > 1 for row in labels),
        "labels": labels,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="HEAD", help="Git commit or ref to audit (default: HEAD)")
    args = parser.parse_args()
    try:
        revision = resolve_revision(args.revision)
        registries = {
            path: yaml.safe_load(git("show", f"{revision}:{path}"))[collection]
            for _, path, collection, _, prefix, _ in TARGETS
            if prefix in SCOPE_PREFIXES
        }
        territories = yaml.safe_load(git("show", f"{revision}:knowledge/TERRITORIES.yml"))["territories"]
        report = {"revision": revision, **geographic_inventory(registries, territories)}
    except subprocess.CalledProcessError as exc:
        parser.error(exc.stderr.strip() or "unable to read the requested Git revision")
    except (KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        parser.error(f"invalid geographic inventory input: {exc}")
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
