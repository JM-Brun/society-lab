#!/usr/bin/env python3
"""Audit the internal arithmetic consistency of the 1970–1993 SMIC transcription.

This is a diagnostic, not a reconstruction of the legal formula. It deliberately
does not sum or compound percentage components: the source's conventions and
rounding must be reconciled before such operations are justified.
"""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "smic-revaluations-1970-1993.csv"
TOLERANCE_PP = Decimal("0.15")
NUMERIC_FIELDS = (
    "observed_change_pct",
    "price_component_pct",
    "half_tsh_component_pct",
    "legal_obligation_pct",
    "discretionary_boost_pct",
)


def audit_rows(rows: list[dict[str, str]]) -> dict:
    if not rows:
        raise ValueError("dataset is empty")
    required = {"period", "date_effective", "source_id", *NUMERIC_FIELDS}
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"missing columns: {', '.join(sorted(missing))}")

    observed_gaps = []
    legal_gaps = []
    periods = set()
    previous_date = None
    source_ids = set()

    for row in rows:
        period = row["period"]
        if period in periods:
            raise ValueError(f"duplicate period: {period}")
        periods.add(period)
        effective_date = row["date_effective"]
        if previous_date is not None and effective_date < previous_date:
            raise ValueError(f"dates are not ordered at {period}")
        previous_date = effective_date
        source_ids.add(row["source_id"])

        values = {field: Decimal(row[field]) for field in NUMERIC_FIELDS}
        observed_gap = values["observed_change_pct"] - values["legal_obligation_pct"] - values["discretionary_boost_pct"]
        legal_gap = values["legal_obligation_pct"] - values["price_component_pct"] - values["half_tsh_component_pct"]
        if abs(observed_gap) > TOLERANCE_PP:
            observed_gaps.append({"period": period, "gap_pp": observed_gap})
        if abs(legal_gap) > TOLERANCE_PP:
            legal_gaps.append({"period": period, "gap_pp": legal_gap})

    if len(source_ids) != 1:
        raise ValueError(f"expected one source identifier, found {sorted(source_ids)}")

    return {
        "row_count": len(rows),
        "first_period": rows[0]["period"],
        "last_period": rows[-1]["period"],
        "source_id": next(iter(source_ids)),
        "tolerance_pp": TOLERANCE_PP,
        "observed_vs_legal_plus_boost": observed_gaps,
        "legal_vs_price_plus_half_tsh": legal_gaps,
    }


def main() -> int:
    with CSV_PATH.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    result = audit_rows(rows)

    print("Audit arithmétique de la transcription historique du SMIC")
    print(f"Lignes : {result['row_count']} ({result['first_period']} à {result['last_period']})")
    print(f"Source : {result['source_id']}")
    print(f"Seuil de signalement : {result['tolerance_pp']} point de pourcentage")
    for label, key in (
        ("Hausse observée − obligation légale − coup de pouce déclaré", "observed_vs_legal_plus_boost"),
        ("Obligation légale − composante prix − moitié TSH", "legal_vs_price_plus_half_tsh"),
    ):
        gaps = result[key]
        max_gap = max((abs(item["gap_pp"]) for item in gaps), default=Decimal("0"))
        print(f"{label} : {len(gaps)} écart(s) au-delà du seuil ; écart absolu maximal {max_gap} point(s)")
        for item in gaps:
            print(f"  - {item['period']}: {item['gap_pp']} point(s)")

    print("\nInterprétation : ces écarts signalent des conventions, arrondis ou transcriptions à réconcilier.")
    print("Ils ne prouvent pas une erreur de source et ne doivent pas être convertis en sommes cumulées.")
    print("Aucune somme ou composition des taux n'est calculée par ce script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
