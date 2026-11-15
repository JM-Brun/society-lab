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

    def test_published_benchmark_coverage(self):
        result = audit_rows(self.rows)
        self.assertEqual(result["row_count"], 9)
        self.assertEqual(result["years"][0], "1990")
        self.assertEqual(result["years"][-1], "2013")

    def test_rejects_invented_or_missing_year(self):
        rows = [dict(row) for row in self.rows]
        rows[1]["year"] = "1994"
        with self.assertRaisesRegex(ValueError, "benchmark years"):
            audit_rows(rows)

    def test_requires_source_traceability(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["source_url"] = ""
        with self.assertRaisesRegex(ValueError, "source traceability"):
            audit_rows(rows)

    def test_requires_definition_break_note(self):
        rows = [dict(row) for row in self.rows]
        rows[-1]["notes"] = "annual value"
        with self.assertRaisesRegex(ValueError, "definition break"):
            audit_rows(rows)


if __name__ == "__main__":
    unittest.main()
