#!/usr/bin/env python3
"""Descriptive, formation-level analysis of the official Parcoursup 2025 CSV.

Uses only the Python standard library. It does not estimate individual-level
admission probabilities and does not treat sums across formations as unique people.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import median

REQUIRED = {
    "session", "region_etab_aff", "fili", "select_form", "capa_fin",
    "nb_voe_pp", "nb_cla_pp", "prop_tot", "acc_tot",
    "nb_voe_pp_bg", "nb_voe_pp_bt", "nb_voe_pp_bp",
    "nb_cla_pp_bg", "nb_cla_pp_bt", "nb_cla_pp_bp",
    "acc_neobac", "acc_bg", "acc_bt", "acc_bp",
    "nb_voe_pp_bg_brs", "nb_voe_pp_bt_brs", "nb_voe_pp_bp_brs", "acc_brs",
}

NUMERIC_FIELDS = (
    "capa_fin", "nb_voe_pp", "nb_cla_pp", "prop_tot", "acc_tot", "acc_pp", "acc_pc",
    "nb_voe_pp_bg", "nb_voe_pp_bt", "nb_voe_pp_bp",
    "nb_cla_pp_bg", "nb_cla_pp_bt", "nb_cla_pp_bp",
    "acc_neobac", "acc_bg", "acc_bt", "acc_bp",
    "nb_voe_pp_bg_brs", "nb_voe_pp_bt_brs", "nb_voe_pp_bp_brs", "acc_brs",
)
NUMERIC = set(NUMERIC_FIELDS)
GROUPS = {
    "region": "region_etab_aff",
    "filiere": "fili",
    "select_form_raw": "select_form",
}


def number(value: str | None) -> float | None:
    if value is None or value.strip() == "":
        return None
    cleaned = value.strip().replace("\u00a0", "").replace(" ", "").replace(",", ".")
    try:
        result = float(cleaned)
    except ValueError:
        return None
    return result if math.isfinite(result) else None


def ratio(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator is None or denominator == 0:
        return None
    return numerator / denominator


def quantile(values: list[float], probability: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def sum_complete(rows: list[dict], key: str) -> float | None:
    values = [r[key] for r in rows]
    if not values or any(value is None for value in values):
        return None
    return sum(values)


def profile(rows: list[dict]) -> dict:
    sums = {key: sum_complete(rows, key) for key in NUMERIC}
    result = {
        "formations": len(rows),
        "capacity": sums["capa_fin"],
        "wishes_phase_principale": sums["nb_voe_pp"],
        "classified_phase_principale": sums["nb_cla_pp"],
        "proposals_total": sums["prop_tot"],
        "accepted_candidates_total": sums["acc_tot"],
        "accepted_phase_principale": sums["acc_pp"],
        "accepted_phase_complementaire": sums["acc_pc"],
        "demand_per_seat": ratio(sums["nb_voe_pp"], sums["capa_fin"]),
        "classified_over_wishes": ratio(sums["nb_cla_pp"], sums["nb_voe_pp"]),
        "pp_acceptances_over_pp_wishes": ratio(sums["acc_pp"], sums["nb_voe_pp"]),
        "accepted_campaign_over_capacity": ratio(sums["acc_tot"], sums["capa_fin"]),
    }
    bac_candidates = {
        "general": sums["nb_voe_pp_bg"],
        "technological": sums["nb_voe_pp_bt"],
        "vocational": sums["nb_voe_pp_bp"],
    }
    bac_classified = {
        "general": sums["nb_cla_pp_bg"],
        "technological": sums["nb_cla_pp_bt"],
        "vocational": sums["nb_cla_pp_bp"],
    }
    bac_admitted = {
        "general": sums["acc_bg"],
        "technological": sums["acc_bt"],
        "vocational": sums["acc_bp"],
    }
    candidates_total = (sum(bac_candidates.values()) if all(v is not None for v in bac_candidates.values()) else None)
    classified_total = (sum(bac_classified.values()) if all(v is not None for v in bac_classified.values()) else None)
    admitted_total = sums["acc_neobac"]
    for track, value in bac_candidates.items():
        result[f"candidate_share_{track}_among_new_bac_pp"] = ratio(value, candidates_total)
    for track, value in bac_classified.items():
        result[f"classified_share_{track}_among_new_bac"] = ratio(value, classified_total)
    for track, value in bac_admitted.items():
        result[f"admitted_share_{track}_among_new_bac"] = ratio(value, admitted_total)

    bursary_candidates = [
        sums["nb_voe_pp_bg_brs"], sums["nb_voe_pp_bt_brs"], sums["nb_voe_pp_bp_brs"]
    ]
    bursary_candidates_total = (
        sum(bursary_candidates)
        if all(v is not None for v in bursary_candidates) else None
    )
    result["bursary_share_candidates_new_bac_pp"] = ratio(
        bursary_candidates_total, candidates_total
    )
    result["bursary_share_admitted_new_bac"] = ratio(sums["acc_brs"], admitted_total)
    return result


def load_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        sample = handle.read(8192)
        handle.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=";,\t")
        except csv.Error:
            dialect = csv.excel
        reader = csv.DictReader(handle, dialect=dialect)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header row")
        missing = sorted(REQUIRED - set(reader.fieldnames))
        if missing:
            raise ValueError("Missing required columns: " + ", ".join(missing))
        rows = []
        for line_no, raw in enumerate(reader, start=2):
            if not raw.get("session"):
                continue
            if raw["session"].strip() != "2025":
                raise ValueError(f"Unexpected session at CSV line {line_no}: {raw['session']!r}")
            row = {key: (raw.get(key) or "").strip() for key in GROUPS.values()}
            row.update({key: number(raw.get(key)) for key in NUMERIC})
            row["lib_for_voe_ins"] = (raw.get("lib_for_voe_ins") or "").strip()
            rows.append(row)
    if not rows:
        raise ValueError("No Parcoursup 2025 records found")
    return rows


def grouped(rows: list[dict], key: str) -> list[dict]:
    buckets = defaultdict(list)
    for row in rows:
        label = row[key] or "[missing]"
        buckets[label].append(row)
    return [{"group": label, **profile(members)} for label, members in sorted(buckets.items())]


def write_csv(path: Path, records: list[dict]) -> None:
    if not records:
        return
    fields = list(records[0])
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)


def run(input_path: Path, output_dir: Path) -> dict:
    rows = load_rows(input_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    for label, column in GROUPS.items():
        write_csv(output_dir / f"by_{label}.csv", grouped(rows, column))

    per_formation = []
    for row in rows:
        per_formation.append({
            "formation": row.get("lib_for_voe_ins", ""),
            "region": row.get("region_etab_aff", ""),
            "filiere": row.get("fili", ""),
            "select_form_raw": row.get("select_form", ""),
            "demand_per_seat": ratio(row["nb_voe_pp"], row["capa_fin"]),
            "classified_over_wishes": ratio(row["nb_cla_pp"], row["nb_voe_pp"]),
            "pp_acceptances_over_pp_wishes": ratio(row["acc_pp"], row["nb_voe_pp"]),
            "accepted_campaign_over_capacity": ratio(row["acc_tot"], row["capa_fin"]),
        })
    write_csv(output_dir / "formation_indicators.csv", per_formation)

    demand_values = [r["demand_per_seat"] for r in per_formation if r["demand_per_seat"] is not None]
    manifest = {
        "dataset": "Parcoursup 2025 — fr-esr-parcoursup",
        "source_file": input_path.name,
        "records": len(rows),
        "missing_values_by_variable": {key: sum(row[key] is None for row in rows) for key in NUMERIC_FIELDS},
        "unit_of_observation": "formation / établissement",
        "warning": (
            "Aggregating counts across formations counts candidate-formation records or wishes, "
            "not unique people. The bursary applicant share (phase principale) and admitted "
            "share (campaign-wide admissions) have different population/time bases and are not "
            "an admission rate or causal effect."
        ),
        "selectivity": "Raw select_form values retained; do not infer labels without codebook validation.",
        "demand_per_seat_distribution": {
            "n_non_missing": len(demand_values),
            "minimum": min(demand_values) if demand_values else None,
            "p25": quantile(demand_values, 0.25),
            "median": median(demand_values) if demand_values else None,
            "p75": quantile(demand_values, 0.75),
            "maximum": max(demand_values) if demand_values else None,
        },
        "outputs": [
            "by_region.csv", "by_filiere.csv", "by_select_form_raw.csv",
            "formation_indicators.csv",
        ],
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Official source CSV")
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.input, args.output_dir), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
