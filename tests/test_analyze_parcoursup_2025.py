import csv
import tempfile
import unittest
from pathlib import Path

from scripts.analysis.analyze_parcoursup_2025 import (
    load_rows, number, profile, quantile, ratio,
)


class ParcoursupAnalysisTests(unittest.TestCase):
    def test_number_handles_french_numeric_formats_and_missing(self):
        self.assertEqual(number("1 234,5"), 1234.5)
        self.assertIsNone(number(""))
        self.assertIsNone(number("not-a-number"))

    def test_ratio_preserves_missing_and_zero_denominators(self):
        self.assertIsNone(ratio(2, 0))
        self.assertIsNone(ratio(None, 2))
        self.assertEqual(ratio(1, 4), 0.25)

    def test_quantile_uses_linear_interpolation(self):
        self.assertEqual(quantile([1, 2, 3, 4], 0.25), 1.75)
        self.assertIsNone(quantile([], 0.5))

    def test_profile_does_not_turn_missing_values_into_zero(self):
        row = {
            "capa_fin": 10, "nb_voe_pp": 20, "nb_cla_pp": 15,
            "prop_tot": 12, "acc_tot": 8, "acc_pp": 6, "acc_pc": 2,
            "nb_voe_pp_bg": 10, "nb_voe_pp_bt": 5, "nb_voe_pp_bp": 5,
            "nb_cla_pp_bg": 8, "nb_cla_pp_bt": 4, "nb_cla_pp_bp": 3,
            "acc_neobac": 6, "acc_bg": 4, "acc_bt": 1, "acc_bp": 1,
            "nb_voe_pp_bg_brs": 2, "nb_voe_pp_bt_brs": 1,
            "nb_voe_pp_bp_brs": 1, "acc_brs": 2,
        }
        result = profile([row])
        self.assertEqual(result["demand_per_seat"], 2)
        self.assertEqual(result["bursary_share_candidates_new_bac_pp"], 0.2)
        row["nb_voe_pp_bg"] = None
        self.assertIsNone(profile([row])["candidate_share_general_among_new_bac_pp"])

    def test_load_rows_accepts_api_snake_case_headers_and_checks_session(self):
        fields = [
            "session", "region_etab_aff", "fili", "select_form", "capa_fin",
            "nb_voe_pp", "nb_cla_pp", "prop_tot", "acc_tot", "acc_pp", "acc_pc",
            "nb_voe_pp_bg", "nb_voe_pp_bt", "nb_voe_pp_bp",
            "nb_cla_pp_bg", "nb_cla_pp_bt", "nb_cla_pp_bp",
            "acc_neobac", "acc_bg", "acc_bt", "acc_bp",
            "nb_voe_pp_bg_brs", "nb_voe_pp_bt_brs", "nb_voe_pp_bp_brs", "acc_brs",
        ]
        row = {field: "1" for field in fields}
        row.update({"session": "2025", "region_etab_aff": "Bretagne", "fili": "Licence"})
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields, delimiter=";")
                writer.writeheader()
                writer.writerow(row)
            loaded = load_rows(path)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["fili"], "Licence")
        self.assertEqual(loaded[0]["nb_voe_pp"], 1)

if __name__ == "__main__":
    unittest.main()
