import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "validate"))
from calculate_project_kpis import (
    build_known_ids, calculate_claim_conclusion_coverage,
    calculate_source_coverage, inspect_relations,
)

class ProjectKpiTests(unittest.TestCase):
    def setUp(self):
        self.edge = {"id": "REL-EDGE-A", "type": "REL-INCLUDES",
                     "from": "DOSSIER-A", "to": "SOURCE-A",
                     "justification": "Le dossier mobilise cette source."}

    def test_source_coverage_counts_valid_documentary_relations_in_either_direction(self):
        sources = [{"id": "SOURCE-A"}, {"id": "SOURCE-B"}, {"id": "SOURCE-C"}]
        relations = [self.edge,
            {**self.edge, "id": "REL-EDGE-B", "from": "SOURCE-B", "to": "CLAIM-A", "type": "REL-SUPPORTS"},
            {**self.edge, "id": "REL-EDGE-C", "from": "SOURCE-C", "to": "DOMAIN-A", "type": "REL-ABOUT"}]
        result = calculate_source_coverage(sources, relations,
            {"SOURCE-A", "SOURCE-B", "SOURCE-C", "DOSSIER-A", "CLAIM-A", "DOMAIN-A"})
        self.assertEqual((result["numerator"], result["denominator"]), (2, 3))
        self.assertEqual(result["uncovered_source_ids"], ["SOURCE-C"])

    def test_about_only_does_not_count(self):
        result = calculate_source_coverage([{"id": "SOURCE-A"}],
            [{**self.edge, "type": "REL-ABOUT"}], {"DOSSIER-A", "SOURCE-A"})
        self.assertEqual(result["numerator"], 0)

    def test_invalid_edges_do_not_count(self):
        relations = [{**self.edge, "justification": " "},
                     {**self.edge, "id": "REL-EDGE-B", "to": "SOURCE-MISSING"}]
        result = calculate_source_coverage([{"id": "SOURCE-A"}], relations,
                                           {"DOSSIER-A", "SOURCE-A"})
        self.assertEqual(result["numerator"], 0)
        self.assertEqual(result["unknown_count"], 2)

    def test_empty_source_register_is_not_computable(self):
        result = calculate_source_coverage([], [], set())
        self.assertEqual(result["status"], "not_computable")
        self.assertIsNone(result["value"])

    def test_duplicate_edge_id_is_reported_and_second_edge_excluded(self):
        valid, diagnostics = inspect_relations([self.edge, self.edge], {"DOSSIER-A", "SOURCE-A"})
        self.assertEqual(len(valid), 1)
        self.assertEqual(diagnostics["duplicate_ids"], ["REL-EDGE-A"])

    def test_claim_statuses_count_conclusions_but_exclude_superseded(self):
        claims = [{"id": "CLAIM-A", "status": "supported"},
                  {"id": "CLAIM-B", "status": "partially_supported"},
                  {"id": "CLAIM-C", "status": "contested"},
                  {"id": "CLAIM-D", "status": "not_supported"},
                  {"id": "CLAIM-E", "status": "insufficient_evidence"},
                  {"id": "CLAIM-F", "status": "under_review"},
                  {"id": "CLAIM-G", "status": "superseded"}]
        result = calculate_claim_conclusion_coverage(claims)
        self.assertEqual((result["numerator"], result["denominator"]), (5, 6))
        self.assertEqual(result["excluded_count"], 1)

    def test_unknown_claim_status_is_reported(self):
        result = calculate_claim_conclusion_coverage([{"id": "CLAIM-A", "status": "mystery"}])
        self.assertEqual(result["numerator"], 0)
        self.assertEqual(result["unknown_count"], 1)

    def test_no_active_claims_is_not_computable(self):
        result = calculate_claim_conclusion_coverage([{"id": "CLAIM-A", "status": "superseded"}])
        self.assertEqual(result["status"], "not_computable")
        self.assertIsNone(result["value"])

    def test_known_ids_include_synthesis_registry_identifiers(self):
        data = {"registries": {"sources": [{"id": "SOURCE-A"}]},
                "domains": [{"id": "DOMAIN-A"}], "territories": [{"id": "TERRITORY-A"}],
                "synthesis_entries": [{"synthesis_id": "SYNTHESIS-A"}, {"synthesis_id": "SYNTHESIS-A"}]}
        known, duplicates = build_known_ids(data)
        self.assertEqual(known, {"SOURCE-A", "DOMAIN-A", "TERRITORY-A", "SYNTHESIS-A"})
        self.assertEqual(duplicates, [])

if __name__ == "__main__":
    unittest.main()
