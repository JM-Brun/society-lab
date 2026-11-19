import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"


def load_validator(name):
    schema = json.loads((SCHEMAS / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)


class MechanismConditionalSchemaTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator("mechanism.schema.json")
        self.record = {
            "id": "MECHANISM-EXAMPLE",
            "label": "Example",
            "description": "A sufficiently detailed mechanism description.",
            "domain_ids": ["DOMAIN-ECONOMY"],
            "status": "candidate",
            "reviewed_at": "2026-11-19",
        }

    def test_candidate_status_does_not_require_evidence_links(self):
        self.assertEqual(list(self.validator.iter_errors(self.record)), [])

    def test_supported_status_requires_at_least_one_evidence_link(self):
        record = {**self.record, "status": "supported_in_scope"}
        errors = list(self.validator.iter_errors(record))
        self.assertTrue(any("anyOf" in error.message for error in errors))

    def test_supported_status_accepts_a_claim_link(self):
        record = {**self.record, "status": "supported_in_scope", "claim_ids": ["CLAIM-EXAMPLE"]}
        self.assertEqual(list(self.validator.iter_errors(record)), [])


class IngestionBatchConditionalSchemaTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator("ingestion-batch.schema.json")
        self.batch = {
            "batch_id": "BATCH-EXAMPLE",
            "created_at": "2026-11-19T10:00:00Z",
            "origin": {"kind": "manual_search", "description": "Recherche ciblée"},
            "selection_criteria": {"include": ["source pertinente"], "exclude": ["hors périmètre"]},
            "status": "open",
            "candidates": [{
                "candidate_id": "CANDIDATE-EXAMPLE",
                "decision": "selected",
                "discovered_at": "2026-11-19T10:00:00Z",
                "title": "Source candidate",
                "source_id": "SOURCE-EXAMPLE",
            }],
        }

    def test_selected_candidate_requires_source_id(self):
        record = json.loads(json.dumps(self.batch))
        del record["candidates"][0]["source_id"]
        self.assertTrue(list(self.validator.iter_errors(record)))

    def test_duplicate_candidate_requires_duplicate_of(self):
        record = json.loads(json.dumps(self.batch))
        candidate = record["candidates"][0]
        candidate["decision"] = "duplicate"
        del candidate["source_id"]
        self.assertTrue(list(self.validator.iter_errors(record)))
        candidate["duplicate_of"] = "SOURCE-EXISTING"
        self.assertEqual(list(self.validator.iter_errors(record)), [])

    def test_excluded_candidate_requires_decision_reason(self):
        record = json.loads(json.dumps(self.batch))
        candidate = record["candidates"][0]
        candidate["decision"] = "excluded"
        del candidate["source_id"]
        self.assertTrue(list(self.validator.iter_errors(record)))
        candidate["decision_reason"] = "Hors du périmètre défini"
        self.assertEqual(list(self.validator.iter_errors(record)), [])

    def test_inaccessible_candidate_requires_reason_and_access_status(self):
        record = json.loads(json.dumps(self.batch))
        candidate = record["candidates"][0]
        candidate["decision"] = "inaccessible"
        del candidate["source_id"]
        self.assertTrue(list(self.validator.iter_errors(record)))
        candidate["decision_reason"] = "Texte intégral non accessible"
        candidate["access_status"] = "paywalled"
        self.assertEqual(list(self.validator.iter_errors(record)), [])

    def test_closed_batch_requires_closed_at_and_reviewed_at(self):
        record = json.loads(json.dumps(self.batch))
        record["status"] = "closed"
        self.assertTrue(list(self.validator.iter_errors(record)))
        record["closed_at"] = "2026-11-19T12:00:00Z"
        record["reviewed_at"] = "2026-11-19"
        self.assertEqual(list(self.validator.iter_errors(record)), [])


if __name__ == "__main__":
    unittest.main()
