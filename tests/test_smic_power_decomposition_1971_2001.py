import csv
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "analysis"))
from audit_smic_power_decomposition_1971_2001 import audit_rows
class SmicPowerDecompositionTests(unittest.TestCase):
    def setUp(self):
        path = ROOT / "data" / "smic-real-power-decomposition-1971-2001.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            self.rows = list(csv.DictReader(stream))
    def test_complete_published_coverage(self):
        result = audit_rows(self.rows)
        self.assertEqual(result["row_count"], 31)
        self.assertEqual(result["first_year"], 1971)
        self.assertEqual(result["last_year"], 2001)
    def test_rejects_missing_year(self):
        with self.assertRaisesRegex(ValueError, "unique, ordered"):
            audit_rows(self.rows[:-1])
    def test_requires_traceability(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["source_url"] = ""
        with self.assertRaisesRegex(ValueError, "traceability"):
            audit_rows(rows)
if __name__ == "__main__":
    unittest.main()
