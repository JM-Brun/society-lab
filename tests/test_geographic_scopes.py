import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "audit"))

from report_geographic_scopes import geographic_inventory


class GeographicScopesTests(unittest.TestCase):
    def test_inventory_preserves_labels_and_distinguishes_exact_matches(self):
        registries = {
            "sources": [
                {"id": "SOURCE-B", "geographic_scope": ["France", "France hors Mayotte", "france"]},
                {"id": "SOURCE-A", "geographic_scope": ["France", "Europe"]},
                {"id": "SOURCE-C"},
            ]
        }
        territories = [
            {"id": "TERRITORY-FRANCE", "label": "France"},
            {"id": "TERRITORY-EUROPE-2", "label": "Europe"},
            {"id": "TERRITORY-EUROPE-1", "label": "Europe"},
        ]
        result = geographic_inventory(registries, territories)
        self.assertEqual(result["registries"]["sources"], {"records": 3, "populated": 2, "values": 5})
        self.assertEqual(result["distinct_labels"], 4)
        self.assertEqual(result["labels_with_exact_match"], 2)
        self.assertEqual(result["labels_with_multiple_exact_matches"], 1)
        labels = {row["label"]: row for row in result["labels"]}
        self.assertEqual(labels["France"]["record_ids"], ["SOURCE-A", "SOURCE-B"])
        self.assertEqual(labels["France"]["count"], 2)
        self.assertEqual(labels["France"]["exact_territory_ids"], ["TERRITORY-FRANCE"])
        self.assertEqual(labels["Europe"]["exact_territory_ids"], ["TERRITORY-EUROPE-1", "TERRITORY-EUROPE-2"])
        self.assertEqual(labels["France hors Mayotte"]["exact_territory_ids"], [])
        self.assertEqual(labels["france"]["exact_territory_ids"], [])
        self.assertEqual(result, geographic_inventory(registries, list(reversed(territories))))

    def test_malformed_scope_is_reported_with_the_record_id(self):
        for value in ("France", ["France", None], [" "]):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "SOURCE-A"):
                geographic_inventory({"sources": [{"id": "SOURCE-A", "geographic_scope": value}]}, [])
