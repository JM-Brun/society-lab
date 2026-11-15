#!/usr/bin/env python3
"""Audit the 1996–2008 DARES SMIC decomposition transcription.

The source reports annual July-to-July changes, not necessarily a July-only
increase. The audit checks transcription arithmetic and metadata; it does not
infer legal components or treat residuals as economic effects.
"""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "smic-revaluations-1996-2008.csv"
COMPONENT_FIELDS = (
    "half_real_SHBO_pct",
    "price_component_pct",
    "discretionary_boost_pct",
    "gmr_convergence_pct",
    "gmr_alignment_pct",
)


def audit_rows(rows: list[dict[str, str]]) -> dict:
    if not rows:
        raise ValueError("dataset is empty")
    required = {
        "effective_date", "change_basis", "hourly_gross", "currency",
        "observed_change_pct", "rounding_residual_pct", *COMPONENT_FIELDS,
        "source_note", "source_url", "confidence",
    }
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"missing columns: {', '.join(sorted(missing))}")

    seen_dates: set[str] = set()
    residuals: list[Decimal] = []
    previous_date = None
    for row in rows:
        date = row["effective_date"]
        if date in seen_dates:
            raise ValueError(f"duplicate effective date: {date}")
        seen_dates.add(date)
        if previous_date is not None and date < previous_date:
            raise ValueError(f"dates are not ordered at {date}")
        previous_date = date
        if row["change_basis"] != "annual_glissement_at_july_date":
            raise ValueError(f"unexpected change basis at {date}: {row['change_basis']}")
        if row["currency"] not in {"FRF", "EUR"}:
            raise ValueError(f"unexpected currency at {date}: {row['currency']}")
        if row["confidence"] != "high" or not row["source_url"]:
            raise ValueError(f"missing source traceability at {date}")

        observed = Decimal(row["observed_change_pct"])
        declared_residual = Decimal(row["rounding_residual_pct"])
        component_sum = sum(
            (Decimal(row[field]) for field in COMPONENT_FIELDS if row[field].strip()),
            Decimal("0"),
        )
        calculated_residual = observed - component_sum
        if calculated_residual != declared_residual:
            raise ValueError(
                f"residual mismatch at {date}: declared {declared_residual}, "
                f"calculated {calculated_residual}"
            )
        residuals.append(abs(declared_residual))

    if len(rows) != 13:
        raise ValueError(f"expected 13 annual rows, found {len(rows)}")
    if rows[0]["effective_date"] != "1996-07-01" or rows[-1]["effective_date"] != "2008-07-01":
        raise ValueError("unexpected first or last date")

    gmr_rows = {row["effective_date"]: row for row in rows if row["gmr_convergence_pct"].strip()}
    if set(gmr_rows) != {"2003-07-01", "2004-07-01", "2005-07-01"}:
        raise ValueError(f"unexpected GMR convergence dates: {sorted(gmr_rows)}")

    may_1996 = next(row for row in rows if row["effective_date"] == "1996-07-01")
    may_2008 = next(row for row in rows if row["effective_date"] == "2008-07-01")
    if "May 1996" not in may_1996["source_note"] or "May 2008" not in may_2008["source_note"]:
        raise ValueError("annual July glissements do not document May adjustments")

    return {
        "row_count": len(rows),
        "first_date": rows[0]["effective_date"],
        "last_date": rows[-1]["effective_date"],
        "max_abs_residual_pp": max(residuals),
        "gmr_convergence_dates": sorted(gmr_rows),
    }


def main() -> int:
    with CSV_PATH.open(encoding="utf-8", newline="") as stream:
        result = audit_rows(list(csv.DictReader(stream)))
    print("Audit de la décomposition annuelle DARES du SMIC (1996–2008)")
    print(f"Lignes : {result['row_count']} ({result['first_date']} à {result['last_date']})")
    print(f"Résidu absolu maximal conservé : {result['max_abs_residual_pp']} point(s)")
    print("Convergence GMR : " + ", ".join(result["gmr_convergence_dates"]))
    print("Les variations sont des glissements annuels à date de juillet, pas des hausses de juillet isolées.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
