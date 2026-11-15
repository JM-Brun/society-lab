import csv
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "analysis"))
from audit_smic_real_purchasing_power_historical_benchmarks import audit_rows

class HistoricalSmicPurchasingPowerTests(unittest.TestCase):
    def setUp(self):
        path = ROOT / "data" / "smic-real-purchasing-power-historical-benchmarks.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            self.rows = list(csv.DictReader(stream))

    def test_published_benchmark_coverage_and_order(self):
        result = audit_rows(self.rows)
        self.assertEqual(result["row_count"], 16)
        self.assertEqual(result["years"], sorted(set(result["years"])))

    def test_requires_source_traceability(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["source_url"] = ""
        with self.assertRaisesRegex(ValueError, "source traceability"):
            audit_rows(rows)

    def test_requires_definition_break_note(self):
        rows = [dict(row) for row in self.rows]
        next(r for r in rows if r["year"] == "2013")["notes"] = "annual value"
        with self.assertRaisesRegex(ValueError, "definition break"):
            audit_rows(rows)

    def test_requires_tef_2010_vintage(self):
        rows = [dict(row) for row in self.rows]
        next(r for r in rows if r["source_id"] == "SOURCE-INSEE-SMIC-POWER-TEF2010")["notes"] = "annual value"
        with self.assertRaisesRegex(ValueError, "TEF 2010 vintage"):
            audit_rows(rows)

if __name__ == "__main__":
    unittest.main()
