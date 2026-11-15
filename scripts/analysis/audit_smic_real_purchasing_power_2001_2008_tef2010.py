import csv
from decimal import Decimal
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
CSV_PATH = ROOT / "data" / "smic-real-purchasing-power-2001-2008-tef2010.csv"
EXPECTED = [str(y) for y in range(2001, 2009)]
FIELDS = ("smic_hourly_gross_annual_avg_eur","purchasing_power_change_gross_pct","purchasing_power_change_net_pct","shbo_purchasing_power_change_pct","annual_cpi_change_pct")
def audit_rows(rows):
    if [r["year"] for r in rows] != EXPECTED:
        raise ValueError("years must be unique, ordered and cover 2001-2008")
    for r in rows:
        if r["source_id"] != "SOURCE-INSEE-TEF-2010-SMIC-POWER" or not r["source_url"]:
            raise ValueError(f"missing source traceability in {r['year']}")
        if r["geographic_scope"] != "France" or r["confidence"] != "high":
            raise ValueError(f"unexpected scope or confidence in {r['year']}")
        for f in FIELDS:
            Decimal(r[f])
    return len(rows)
def main():
    with CSV_PATH.open(encoding="utf-8",newline="") as f:
        print(f"TEF 2010 SMIC purchasing-power audit: {audit_rows(list(csv.DictReader(f)))} rows")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
