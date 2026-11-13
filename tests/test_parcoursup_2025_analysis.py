import csv
import tempfile
import unittest
from pathlib import Path

from scripts.analysis.analyze_parcoursup_2025 import load_rows, profile, quantile, ratio

# Canonical field names exposed by the Explore API 2.1 export.
FIELDS = [
    "session", "region_etab_aff", "fili", "select_form", "capa_fin",
    "nb_voe_pp", "nb_cla_pp", "prop_tot", "acc_tot", "acc_pp", "acc_pc",
    "nb_voe_pp_bg", "nb_voe_pp_bt", "nb_voe_pp_bp",
    "nb_cla_pp_bg", "nb_cla_pp_bt", "nb_cla_pp_bp",
    "acc_neobac", "acc_bg", "acc_bt", "acc_bp",
    "nb_voe_pp_bg_brs", "nb_voe_pp_bt_brs", "nb_voe_pp_bp_brs", "acc_brs",
]


class ParcoursupAnalysisTests(unittest.TestCase):
    def test_zero_denominator_is_missing(self):
        self.assertIsNone(ratio(3, 0))
        self.assertIsNone(ratio(None, 10))

    def test_quantiles_use_interpolated_order_statistics(self):
        self.assertEqual(quantile([1, 2, 3, 4], 0.25), 1.75)
        self.assertIsNone(quantile([], 0.5))

    def test_aggregates_count_formations_not_unique_people(self):
        row = {key: 0 for key in FIELDS}
        row.update({
            "session": "2025", "region_etab_aff": "Bretagne",
            "fili": "BUT", "select_form": "1",
        })
        result = profile([row, row.copy()])
        self.assertEqual(result["formations"], 2)
        self.assertEqual(result["wishes_phase_principale"], 0)

    def test_profiles_keep_distinct_populations(self):
        row = {key: None for key in FIELDS}
        row.update({
            "session": "2025", "region_etab_aff": "Bretagne",
            "fili": "BUT", "select_form": "1", "capa_fin": 10,
            "nb_voe_pp": 100, "nb_cla_pp": 50, "prop_tot": 20,
            "acc_tot": 10, "acc_pp": 7, "acc_pc": 3, "nb_voe_pp_bg": 60, "nb_voe_pp_bt": 30,
            "nb_voe_pp_bp": 10, "nb_cla_pp_bg": 30,
            "nb_cla_pp_bt": 15, "nb_cla_pp_bp": 5,
            "acc_neobac": 8, "acc_bg": 5, "acc_bt": 2, "acc_bp": 1,
            "nb_voe_pp_bg_brs": 12, "nb_voe_pp_bt_brs": 9,
            "nb_voe_pp_bp_brs": 5, "acc_brs": 3,
        })
        result = profile([row])
        self.assertAlmostEqual(result["demand_per_seat"], 10)
        self.assertAlmostEqual(result["pp_acceptances_over_pp_wishes"], 0.07)
        self.assertAlmostEqual(result["accepted_campaign_over_capacity"], 1.0)
        self.assertAlmostEqual(result["candidate_share_general_among_new_bac_pp"], 0.6)
        self.assertAlmostEqual(result["admitted_share_general_among_new_bac"], 0.625)
        self.assertAlmostEqual(result["bursary_share_candidates_new_bac_pp"], 0.26)
        self.assertAlmostEqual(result["bursary_share_admitted_new_bac"], 0.375)

    def test_missing_subgroup_count_is_not_silently_zero(self):
        row = {key: 0 for key in FIELDS}
        row.update({
            "session": "2025", "region_etab_aff": "Bretagne",
            "fili": "BUT", "select_form": "1",
        })
        row["nb_voe_pp_bt"] = None
        result = profile([row])
        self.assertIsNone(result["candidate_share_general_among_new_bac_pp"])
        self.assertIsNone(result["bursary_share_candidates_new_bac_pp"])

    def test_csv_rejects_wrong_session(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.csv"
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS)
                writer.writeheader()
                row = {key: "0" for key in FIELDS}
                row["session"] = "2024"
                writer.writerow(row)
            with self.assertRaisesRegex(ValueError, "Unexpected session"):
                load_rows(path)


if __name__ == "__main__":
    unittest.main()
