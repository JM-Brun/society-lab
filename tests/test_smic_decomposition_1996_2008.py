import csv
import sys
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "analysis"))
from audit_smic_decomposition_1996_2008 import audit_rows


class SmicDecomposition1996To2008Tests(unittest.TestCase):
    def setUp(self):
        self.path = ROOT / "data" / "smic-revaluations-1996-2008.csv"
        with self.path.open(encoding="utf-8", newline="") as stream:
            self.rows = list(csv.DictReader(stream))

    def test_dataset_scope_and_gmr_period_are_explicit(self):
        result = audit_rows(self.rows)
        self.assertEqual(result["row_count"], 13)
        self.assertEqual(result["first_date"], "1996-07-01")
        self.assertEqual(result["last_date"], "2008-07-01")
        self.assertEqual(result["gmr_convergence_dates"], [
            "2003-07-01", "2004-07-01", "2005-07-01"
        ])

    def test_residuals_are_recomputed_not_forced_to_zero(self):
        result = audit_rows(self.rows)
        self.assertEqual(result["max_abs_residual_pp"], Decimal("0.110"))
        row_2007 = next(row for row in self.rows if row["effective_date"] == "2007-07-01")
        self.assertEqual(row_2007["rounding_residual_pct"], "0.110")

    def test_1996_and_2008_annual_rows_include_may_changes(self):
        row_1996 = next(row for row in self.rows if row["effective_date"] == "1996-07-01")
        row_2008 = next(row for row in self.rows if row["effective_date"] == "2008-07-01")
        self.assertIn("May 1996", row_1996["source_note"])
        self.assertIn("May 2008", row_2008["source_note"])

    def test_rejects_residual_inconsistency(self):
        rows = [dict(row) for row in self.rows]
        rows[0]["rounding_residual_pct"] = "0.100"
        with self.assertRaisesRegex(ValueError, "residual mismatch"):
            audit_rows(rows)

    def test_rejects_duplicate_dates(self):
        rows = [dict(row) for row in self.rows]
        rows[1]["effective_date"] = rows[0]["effective_date"]
        with self.assertRaisesRegex(ValueError, "duplicate effective date"):
            audit_rows(rows)


if __name__ == "__main__":
    unittest.main()
