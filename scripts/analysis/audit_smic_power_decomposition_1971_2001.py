#!/usr/bin/env python3
"""Audit transcription of the DARES SMIC decomposition, 1971-2001."""
import csv
from decimal import Decimal
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "smic-real-power-decomposition-1971-2001.csv"
EXPECTED_YEARS = list(range(1971, 2002))
FIELDS = ("half_shbo_real_contribution_pct", "discretionary_boost_nominal_contribution_pct")
def audit_rows(rows):
    years = [int(row["year"]) for row in rows]
    if years != EXPECTED_YEARS:
        raise ValueError("years must be unique, ordered and cover 1971-2001")
    for row in rows:
        if row["source_id"] != "SOURCE-DARES-SMIC-POWER-DECOMPOSITION-1971-2001" or not row["source_url"]:
            raise ValueError(f"missing source traceability in {row['year']}")
        if row["geographic_scope"] != "France" or row["confidence"] != "high":
            raise ValueError(f"unexpected scope or confidence in {row['year']}")
        for field in FIELDS:
            Decimal(row[field])
    if "GMR" not in next(row["notes"] for row in rows if row["year"] == "1999"):
        raise ValueError("1999 GMR inclusion note is required")
    return {"row_count": len(rows), "first_year": years[0], "last_year": years[-1]}
def main():
    with CSV_PATH.open(encoding="utf-8", newline="") as stream:
        result = audit_rows(list(csv.DictReader(stream)))
    print(f"DARES decomposition audit: {result['row_count']} rows ({result['first_year']}-{result['last_year']})")
    print("Components remain separate; no observed total or chained index is calculated.")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
