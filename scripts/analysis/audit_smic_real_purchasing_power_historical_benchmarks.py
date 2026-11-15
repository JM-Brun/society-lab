#!/usr/bin/env python3
"""Audit historical INSEE SMIC purchasing-power observations and publication vintages."""
from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "smic-real-purchasing-power-historical-benchmarks.csv"
EXPECTED_YEARS = ["1990", "1995", "2000", "2005", "2009", "2010", "2011", "2012", "2013",
                  "2001", "2002", "2003", "2004", "2006", "2007", "2008"]
# The CSV is sorted chronologically; keep one row per year. The 2005 duplicate
# across source vintages is deliberately not allowed: retain the earlier TEF
# benchmark row and document the TEF 2010 value in its own provenance field.
NUMERIC_FIELDS = (
    "smic_hourly_gross_annual_avg_eur",
    "purchasing_power_change_gross_pct",
    "purchasing_power_change_net_pct",
    "shbo_or_shboe_purchasing_power_change_pct",
    "annual_cpi_change_pct",
)

def audit_rows(rows: list[dict[str, str]]) -> dict:
    years = [row["year"] for row in rows]
    if years != sorted(set(years)):
        raise ValueError("years must be unique and chronologically ordered")
    required = {"1990", "1995", "2000", "2001", "2002", "2003", "2004", "2005",
                "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"}
    if not required.issubset(set(years)):
        raise ValueError("missing a published historical benchmark year")
    for row in rows:
        if row["geographic_scope"] != "France":
            raise ValueError(f"unexpected geographic scope in {row['year']}")
        if row["confidence"] != "high" or not row["source_id"] or not row["source_url"]:
            raise ValueError(f"missing source traceability in {row['year']}")
        for field in NUMERIC_FIELDS:
            if not row[field].strip():
                raise ValueError(f"missing {field} in {row['year']}")
            Decimal(row[field])
        if row["source_id"] == "SOURCE-INSEE-SMIC-POWER-TEF2010" and "TEF 2010" not in row["notes"]:
            raise ValueError(f"missing TEF 2010 vintage note in {row['year']}")
    if "SHBOE replaces SHBO" not in next(r for r in rows if r["year"] == "2013")["notes"]:
        raise ValueError("2013 SHBO/SHBOE definition break must be documented")
    if "historical vintage" not in next(r for r in rows if r["year"] == "2005")["notes"]:
        raise ValueError("2005 historical source vintage must remain explicit")
    return {"row_count": len(rows), "years": years}

def main() -> int:
    with CSV_PATH.open(encoding="utf-8", newline="") as stream:
        result = audit_rows(list(csv.DictReader(stream)))
    print("Audit des observations historiques du pouvoir d'achat du SMIC")
    print(f"Lignes : {result['row_count']} ; années : {', '.join(result['years'])}")
    print("Aucune interpolation ni chaîne d'indice n'est calculée.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
