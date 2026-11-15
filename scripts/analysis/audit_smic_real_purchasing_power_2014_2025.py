#!/usr/bin/env python3
"""Audit the INSEE annual real purchasing-power transcription, 2014–2025."""
from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "smic-real-purchasing-power-2014-2025.csv"


def audit_rows(rows: list[dict[str, str]]) -> dict:
    if len(rows) != 12:
        raise ValueError(f"expected 12 annual rows, found {len(rows)}")
    expected_years = [str(year) for year in range(2014, 2026)]
    if [row["year"] for row in rows] != expected_years:
        raise ValueError("years must be unique, ordered and cover 2014–2025")

    index = Decimal("100")
    max_difference = Decimal("0")
    for i, row in enumerate(rows):
        if row["geographic_scope"] != "France hors Mayotte":
            raise ValueError(f"unexpected geographic scope in {row['year']}")
        if row["confidence"] != "high" or not row["source_url"]:
            raise ValueError(f"missing source traceability in {row['year']}")
        if i == 0:
            expected = Decimal("100")
        else:
            change = Decimal(row["purchasing_power_change_gross_pct"])
            index *= Decimal("1") + change / Decimal("100")
            expected = index.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
        actual = Decimal(row["real_gross_smic_index_2014_100"])
        difference = abs(actual - expected)
        max_difference = max(max_difference, difference)
        if difference > Decimal("0.0001"):
            raise ValueError(
                f"real index mismatch in {row['year']}: {actual} vs {expected}"
            )
    if rows[-1]["year"] != "2025":
        raise ValueError("latest real purchasing-power observation must be 2025")
    if rows[-1]["shboe_purchasing_power_change_pct"].strip():
        raise ValueError("2025 SHBOE value should remain missing as in source")
    return {
        "row_count": len(rows),
        "first_year": rows[0]["year"],
        "last_year": rows[-1]["year"],
        "index_2025": rows[-1]["real_gross_smic_index_2014_100"],
        "max_index_difference": str(max_difference),
    }


def main() -> int:
    with CSV_PATH.open(encoding="utf-8", newline="") as stream:
        result = audit_rows(list(csv.DictReader(stream)))
    print("Audit du pouvoir d'achat annuel du SMIC (INSEE, 2014–2025)")
    print(f"Lignes : {result['row_count']} ({result['first_year']}–{result['last_year']})")
    print(f"Indice chaîné 2014=100 en 2025 : {result['index_2025']}")
    print("Les variations publiées arrondies sont chaînées ; l'indice n'est pas une série INSEE autonome.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
