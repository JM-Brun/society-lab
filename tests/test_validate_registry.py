import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "validate"))

from validate_registry import validate_batch_manifest, validate_cross_references, validate_graph_edges


class CrossReferenceValidationTests(unittest.TestCase):
    def test_checks_dossier_concept_references(self):
        records = {"DOSSIER": [{"id": "DOSSIER-A", "concept_ids": ["CONCEPT-MISSING"]}]}
        node_ids = {"CONCEPT": set()}
        errors = []
        validate_cross_references(records, node_ids, errors)
        self.assertTrue(any("concept_ids" in error and "CONCEPT-MISSING" in error for error in errors))

    def test_checks_nested_claim_source_verifications(self):
        records = {"CLAIM": [{
            "id": "CLAIM-A",
            "source_verifications": [{"source_id": "SOURCE-MISSING", "status": "source_checked"}],
        }]}
        node_ids = {"SOURCE": set()}
        errors = []
        validate_cross_references(records, node_ids, errors)
        self.assertTrue(any("source_verifications.source_id" in error for error in errors))

    def test_accepts_resolved_nested_and_concept_references(self):
        records = {
            "DOSSIER": [{"id": "DOSSIER-A", "concept_ids": ["CONCEPT-A"]}],
            "CLAIM": [{"id": "CLAIM-A", "source_verifications": [{"source_id": "SOURCE-A"}]}],
        }
        node_ids = {"CONCEPT": {"CONCEPT-A"}, "SOURCE": {"SOURCE-A"}}
        errors = []
        validate_cross_references(records, node_ids, errors)
        self.assertEqual(errors, [])


class GraphValidationTests(unittest.TestCase):
    def setUp(self):
        self.relations = {
            "REL-SUPPORTS": {"from": ["STUDY"], "to": ["CLAIM"]},
        }
        self.nodes = {"STUDY-A": "STUDY", "CLAIM-A": "CLAIM"}
        self.edge = {
            "id": "REL-EDGE-A",
            "type": "REL-SUPPORTS",
            "from": "STUDY-A",
            "to": "CLAIM-A",
            "justification": "La source rapporte le résultat dans le périmètre indiqué.",
        }

    def test_accepts_well_formed_edge(self):
        errors = []
        validate_graph_edges([self.edge], self.relations, self.nodes, errors)
        self.assertEqual(errors, [])

    def test_rejects_missing_justification(self):
        edge = {**self.edge, "justification": " "}
        errors = []
        validate_graph_edges([edge], self.relations, self.nodes, errors)
        self.assertTrue(any("missing non-empty relation justification" in error for error in errors))

    def test_rejects_duplicate_relation_triples(self):
        second = {**self.edge, "id": "REL-EDGE-B", "justification": "Une seconde justification."}
        errors = []
        validate_graph_edges([self.edge, second], self.relations, self.nodes, errors)
        self.assertTrue(any("duplicate relation triple" in error for error in errors))

    def test_rejects_unresolved_or_incompatible_endpoints(self):
        edge = {**self.edge, "to": "STUDY-A"}
        errors = []
        validate_graph_edges([edge], self.relations, self.nodes, errors)
        self.assertTrue(any("type STUDY not allowed" in error for error in errors))


class IngestionBatchValidationTests(unittest.TestCase):
    def setUp(self):
        self.batch = {
            "batch_id": "BATCH-EXAMPLE",
            "status": "open",
            "candidates": [
                {"candidate_id": "CANDIDATE-A", "decision": "selected", "source_id": "SOURCE-A"},
                {"candidate_id": "CANDIDATE-B", "decision": "duplicate", "duplicate_of": "CANDIDATE-A"},
            ],
        }

    def test_accepts_resolved_selected_source_and_duplicate(self):
        errors = []
        validate_batch_manifest(self.batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertEqual(errors, [])

    def test_rejects_unresolved_source_id(self):
        batch = {**self.batch, "candidates": [{**self.batch["candidates"][0], "source_id": "SOURCE-MISSING"}]}
        errors = []
        validate_batch_manifest(batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertTrue(any("unresolved source_id" in error for error in errors))

    def test_rejects_unresolved_duplicate_target(self):
        batch = {**self.batch, "candidates": [{**self.batch["candidates"][1], "duplicate_of": "SOURCE-MISSING"}]}
        errors = []
        validate_batch_manifest(batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertTrue(any("unresolved duplicate_of" in error for error in errors))

    def test_rejects_duplicate_candidate_ids(self):
        batch = {**self.batch, "candidates": [
            {"candidate_id": "CANDIDATE-A", "decision": "deferred"},
            {"candidate_id": "CANDIDATE-A", "decision": "deferred"},
        ]}
        errors = []
        validate_batch_manifest(batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertTrue(any("duplicate candidate_id" in error for error in errors))

    def test_closed_batch_cannot_keep_deferred_candidates(self):
        batch = {**self.batch, "status": "closed", "candidates": [
            {"candidate_id": "CANDIDATE-A", "decision": "deferred"},
        ]}
        errors = []
        validate_batch_manifest(batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertTrue(any("closed batch cannot contain deferred" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
