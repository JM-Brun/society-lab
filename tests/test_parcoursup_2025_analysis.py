import csv
import tempfile
import unittest
from pathlib import Path

from scripts.analysis.analyze_parcoursup_2025 import load_rows, profile, ratio

FIELDS = [
    "session", "region_etab_aff", "Fili", "select_form", "capa_fin",
    "nb_VOE_PP", "nb_cla_PP", "Prop_tot", "Acc_tot",
    "nb_VOE_PP_BG", "nb_VOE_PP_BT", "nb_VOE_PP_BP",
    "nb_cla_pp_BG", "nb_cla_pp_BT", "nb_cla_pp_BP",
    "Acc_neobac", "Acc_BG", "Acc_BT", "Acc_BP",
    "nb_VOE_PP_BG_brs", "nb_VOE_PP_BT_brs", "nb_VOE_PP_BP_brs", "Acc_brs",
]

class ParcoursupAnalysisTests(unittest.TestCase):
    def test_zero_denominator_is_missing(self):
        self.assertIsNone(ratio(3, 0))
        self.assertIsNone(ratio(None, 10))

    def test_profiles_keep_distinct_populations(self):
        row = {key: None for key in FIELDS}
        row.update({
            "session": "2025", "region_etab_aff": "Bretagne", "Fili": "BUT",
            "select_form": "1", "capa_fin": 10, "nb_VOE_PP": 100,
            "nb_cla_PP": 50, "Prop_tot": 20, "Acc_tot": 10,
            "nb_VOE_PP_BG": 60, "nb_VOE_PP_BT": 30, "nb_VOE_PP_BP": 10,
            "nb_cla_pp_BG": 30, "nb_cla_pp_BT": 15, "nb_cla_pp_BP": 5,
            "Acc_neobac": 8, "Acc_BG": 5, "Acc_BT": 2, "Acc_BP": 1,
            "nb_VOE_PP_BG_brs": 12, "nb_VOE_PP_BT_brs": 9,
            "nb_VOE_PP_BP_brs": 5, "Acc_brs": 3,
        })
        result = profile([row])
        self.assertAlmostEqual(result["demand_per_seat"], 10)
        self.assertAlmostEqual(result["candidate_share_general_among_new_bac_pp"], 0.6)
        self.assertAlmostEqual(result["admitted_share_general_among_new_bac"], 0.625)
        self.assertAlmostEqual(result["bursary_share_candidates_new_bac_pp"], 0.26)
        self.assertAlmostEqual(result["bursary_share_admitted_new_bac"], 0.375)

    def test_missing_subgroup_count_is_not_silently_zero(self):
        row = {key: 0 for key in FIELDS}
        row.update({"session": "2025", "region_etab_aff": "Bretagne", "Fili": "BUT", "select_form": "1"})
        row["nb_VOE_PP_BT"] = None
        result = profile([row])
        self.assertIsNone(result["candidate_share_general_among_new_bac_pp"])
        self.assertIsNone(result["bursary_share_candidates_new_bac_pp"])

    def test_csv_rejects_wrong_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.csv"
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDS)
                writer.writeheader()
                row = {key: "0" for key in FIELDS}
                row["session"] = "2024"
                writer.writerow(row)
            with self.assertRaisesRegex(ValueError, "Unexpected session"):
                load_rows(path)

if __name__ == "__main__":
    unittest.main()
