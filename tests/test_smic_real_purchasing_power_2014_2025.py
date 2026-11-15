import sys
import unittest
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "analysis"))
from audit_smic_real_purchasing_power_2014_2025 import audit_rows


class SmicRealPurchasingPowerTests(unittest.TestCase):
    def setUp(self):
        path = ROOT / "data" / "smic-real-purchasing-power-2014-2025.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            self.rows = list(csv.DictReader(stream))

    def test_official_series_scope_and_index(self):
        result = audit_rows(self.rows)
        self.assertEqual(result["row_count"], 12)
        self.assertEqual(result["first_year"], "2014")
        self.assertEqual(result["last_year"], "2025")
        self.assertEqual(result["index_2025"], "102.9291")

    def test_detects_wrong_chained_index(self):
        rows = [dict(row) for row in self.rows]
        rows[-1]["real_gross_smic_index_2014_100"] = "104.0000"
        with self.assertRaisesRegex(ValueError, "real index mismatch"):
            audit_rows(rows)

    def test_rejects_missing_year(self):
        with self.assertRaisesRegex(ValueError, "expected 12 annual rows"):
            audit_rows(self.rows[:-1])

    def test_preserves_unavailable_shboe_value(self):
        result = audit_rows(self.rows)
        self.assertEqual(result["last_year"], "2025")
        self.assertEqual(self.rows[-1]["shboe_purchasing_power_change_pct"], "")


if __name__ == "__main__":
    unittest.main()
