import unittest

from tools.smic_openfisca import (
    CASES,
    MONTHS,
    REFERENCE_MONTHLY_GROSS_SMIC,
    build_situation,
)


class SmicOpenFiscaInputTests(unittest.TestCase):
    def test_expected_case_types_are_present(self):
        self.assertEqual(
            [case.identifier for case in CASES],
            [
                "single_full_time",
                "single_parent_part_time",
                "couple_one_low_wage",
                "couple_two_smic",
            ],
        )

    def test_full_time_case_has_twelve_monthly_gross_inputs(self):
        situation = build_situation(CASES[0], REFERENCE_MONTHLY_GROSS_SMIC, 0)
        wage = situation["individus"]["adult_1"]["salaire_de_base"]
        self.assertEqual(set(wage), set(MONTHS))
        self.assertTrue(all(value == REFERENCE_MONTHLY_GROSS_SMIC for value in wage.values()))

    def test_uplift_changes_gross_salary_not_household_composition(self):
        case = CASES[0]
        baseline = build_situation(case, 1000, 0)
        uplifted = build_situation(case, 1000, 0.05)
        self.assertEqual(
            uplifted["individus"]["adult_1"]["salaire_de_base"]["2026-01"],
            1050,
        )
        self.assertEqual(baseline["menages"], uplifted["menages"])

    def test_part_time_profile_is_proportional(self):
        situation = build_situation(CASES[1], 1000, 0)
        wage = situation["individus"]["adult_1"]["salaire_de_base"]["2026-01"]
        self.assertEqual(wage, 800)
        self.assertEqual(len(situation["individus"]), 2)

    def test_negative_salary_uplift_below_minus_100_percent_is_rejected(self):
        with self.assertRaises(ValueError):
            build_situation(CASES[0], 1000, -1.01)

    def test_non_positive_reference_wage_is_rejected(self):
        with self.assertRaises(ValueError):
            build_situation(CASES[0], 0, 0)


if __name__ == "__main__":
    unittest.main()
