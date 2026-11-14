import csv
import sys
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "analysis"))
from audit_smic_revaluations import TOLERANCE_PP, audit_rows


class SmicHistoricalAuditTests(unittest.TestCase):
    def test_historical_transcription_has_24_rows_and_known_periods(self):
        path = ROOT / "data" / "smic-revaluations-1970-1993.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            result = audit_rows(list(csv.DictReader(stream)))
        self.assertEqual(result["row_count"], 24)
        self.assertEqual(result["first_period"], "1970-1971")
        self.assertEqual(result["last_period"], "1993-1994")

    def test_arithmetic_gaps_are_flagged_not_silently_added(self):
        path = ROOT / "data" / "smic-revaluations-1970-1993.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            result = audit_rows(list(csv.DictReader(stream)))
        self.assertEqual(len(result["observed_vs_legal_plus_boost"]), 9)
        self.assertEqual(max(abs(x["gap_pp"]) for x in result["observed_vs_legal_plus_boost"]), Decimal("1.1"))
        self.assertEqual(len(result["legal_vs_price_plus_half_tsh"]), 9)
        self.assertEqual(max(abs(x["gap_pp"]) for x in result["legal_vs_price_plus_half_tsh"]), Decimal("0.4"))
        self.assertEqual(TOLERANCE_PP, Decimal("0.15"))

    def test_rejects_duplicate_periods(self):
        row = {
            "period": "1970-1971", "date_effective": "1970-07-01",
            "source_id": "SOURCE-TEST", "observed_change_pct": "10",
            "price_component_pct": "5", "half_tsh_component_pct": "2",
            "legal_obligation_pct": "7", "discretionary_boost_pct": "3",
        }
        with self.assertRaisesRegex(ValueError, "duplicate period"):
            audit_rows([row, row])


if __name__ == "__main__":
    unittest.main()
