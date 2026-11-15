import csv
import unittest
from pathlib import Path

from scripts.analysis.reconstruct_smic_monthly_purchasing_power import (
    annual_reconstruction,
    link_cpi_series,
    parse_sdmx_observations,
    require_months,
)


class MonthlySmicReconstructionTests(unittest.TestCase):
    def test_parse_structure_specific_sdmx_xml(self):
        xml = b"""<?xml version="1.0"?>
        <mes:DataSet xmlns:mes="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/message"
          xmlns:gen="http://www.sdmx.org/resources/sdmxml/schemas/v2_1/data/structurespecific">
          <gen:Series><gen:Obs TIME_PERIOD="1980-01" OBS_VALUE="2.1025"/>
          <gen:Obs TIME_PERIOD="1980-02" OBS_VALUE="2.1025"/></gen:Series>
        </mes:DataSet>"""
        self.assertEqual(
            parse_sdmx_observations(xml),
            {"1980-01": 2.1025, "1980-02": 2.1025},
        )

    def test_parse_rejects_duplicate_periods(self):
        xml = b"""<DataSet><Series>
        <Obs TIME_PERIOD="1980-01" OBS_VALUE="2"/>
        <Obs TIME_PERIOD="1980-01" OBS_VALUE="2.1"/>
        </Series></DataSet>"""
        with self.assertRaisesRegex(ValueError, "duplicate"):
            parse_sdmx_observations(xml)

    def test_cpi_link_uses_geometric_mean_of_36_overlap_months(self):
        old = {}
        new = {}
        for year in range(1990, 1993):
            for month in range(1, 13):
                period = f"{year}-{month:02d}"
                old[period] = 50.0
                new[period] = 100.0
        old["1989-12"] = 49.0
        linked, factor = link_cpi_series(old, new)
        self.assertEqual(factor, 2.0)
        self.assertEqual(linked["1989-12"], 98.0)
        self.assertEqual(linked["1990-01"], 100.0)

    def test_cpi_link_requires_complete_overlap(self):
        old = {"1990-01": 50.0}
        new = {"1990-01": 100.0}
        with self.assertRaisesRegex(ValueError, "36 months"):
            link_cpi_series(old, new)

    def test_month_coverage_is_strict(self):
        with self.assertRaisesRegex(ValueError, "missing"):
            require_months({"1980-01": 2.0}, 1980, 1980, "SMIC")


    def test_committed_annual_series_has_complete_coverage_and_keypoints(self):
        path = Path(__file__).resolve().parents[1] / "data" / "smic-real-purchasing-power-1970-2025.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            rows = list(csv.DictReader(stream))
        self.assertEqual(len(rows), 56)
        self.assertEqual([row["year"] for row in rows], [str(year) for year in range(1970, 2026)])
        by_year = {row["year"]: row for row in rows}
        self.assertEqual(by_year["1980"]["smic_hourly_gross_annual_avg_eur"], "2.102500")
        self.assertEqual(by_year["2025"]["smic_hourly_gross_annual_avg_eur"], "11.880000")
        self.assertEqual(by_year["2015"]["real_smic_index_2015_100"], "100.000000")
        self.assertAlmostEqual(float(by_year["2025"]["real_smic_index_2015_100"]), 102.206279, places=6)

    def test_annual_formula_uses_ratio_of_annual_means(self):
        smic = {}
        cpi = {}
        for year in range(1970, 2026):
            for month in range(1, 13):
                period = f"{year}-{month:02d}"
                smic[period] = 2.0 if year == 1970 else 4.0
                cpi[period] = 100.0
        rows = annual_reconstruction(smic, cpi)
        self.assertEqual(len(rows), 56)
        self.assertEqual(rows[0]["real_purchasing_power_change_pct"], "")
        self.assertEqual(rows[1]["real_purchasing_power_change_pct"], "100.000000")
        self.assertEqual(rows[1]["smic_nominal_change_pct"], "100.000000")
        self.assertEqual(rows[1]["ipc_inflation_pct"], "0.000000")
        self.assertEqual(rows[-1]["real_smic_index_2015_100"], "100.000000")


if __name__ == "__main__":
    unittest.main()
