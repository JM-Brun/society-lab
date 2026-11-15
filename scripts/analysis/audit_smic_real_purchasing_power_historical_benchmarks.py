#!/usr/bin/env python3
"""Audit the historical INSEE SMIC purchasing-power benchmark transcription."""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "smic-real-purchasing-power-historical-benchmarks.csv"
EXPECTED_YEARS = ["1990", "1995", "2000", "2005", "2009", "2010", "2011", "2012", "2013"]
NUMERIC_FIELDS = (
    "smic_hourly_gross_annual_avg_eur",
    "purchasing_power_change_gross_pct",
    "purchasing_power_change_net_pct",
    "shbo_or_shboe_purchasing_power_change_pct",
    "annual_cpi_change_pct",
)


def audit_rows(rows: list[dict[str, str]]) -> dict:
    if [row["year"] for row in rows] != EXPECTED_YEARS:
        raise ValueError("benchmark years must be unique, ordered and match the published observations")
    for row in rows:
        if row["geographic_scope"] != "France":
            raise ValueError(f"unexpected geographic scope in {row['year']}")
        if row["confidence"] != "high" or not row["source_id"] or not row["source_url"]:
            raise ValueError(f"missing source traceability in {row['year']}")
        for field in NUMERIC_FIELDS:
            if not row[field].strip():
                raise ValueError(f"missing {field} in {row['year']}")
            Decimal(row[field])
    if rows[-1]["year"] != "2013":
        raise ValueError("latest historical observation must be 2013")
    if "SHBOE replaces SHBO" not in rows[-1]["notes"]:
        raise ValueError("2013 SHBO/SHBOE definition break must be documented")
    if "historical vintage" not in rows[3]["notes"]:
        raise ValueError("2005 source vintage must remain explicit")
    return {"row_count": len(rows), "years": EXPECTED_YEARS}


def main() -> int:
    with CSV_PATH.open(encoding="utf-8", newline="") as stream:
        result = audit_rows(list(csv.DictReader(stream)))
    print("Audit des observations historiques du pouvoir d'achat du SMIC")
    print(f"Lignes : {result['row_count']} ; années : {', '.join(result['years'])}")
    print("Aucune interpolation ni chaîne d'indice n'est calculée.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
