import json
import sys
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "validate"))

from validate_registry import (validate_batch_manifest, validate_cross_references, validate_graph_edges,
                                validate_controlled_vocabularies, validate_relation_definitions, validate_territory_hierarchy)


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

class TerritoryHierarchyValidationTests(unittest.TestCase):
    def test_accepts_acyclic_parent_hierarchy(self):
        territories = [{"id": "TERRITORY-A", "geographic_parent_id": "TERRITORY-B"},
                       {"id": "TERRITORY-B"}]
        errors = []
        validate_territory_hierarchy(territories, errors)
        self.assertEqual(errors, [])

    def test_rejects_self_parent(self):
        errors = []
        validate_territory_hierarchy([{"id": "TERRITORY-A", "geographic_parent_id": "TERRITORY-A"}], errors)
        self.assertTrue(any("own geographic parent" in error for error in errors))

    def test_rejects_multi_node_parent_cycle(self):
        territories = [{"id": "TERRITORY-A", "geographic_parent_id": "TERRITORY-B"},
                       {"id": "TERRITORY-B", "geographic_parent_id": "TERRITORY-C"},
                       {"id": "TERRITORY-C", "geographic_parent_id": "TERRITORY-A"}]
        errors = []
        validate_territory_hierarchy(territories, errors)
        self.assertTrue(any("parent cycle" in error for error in errors))


class RelationDefinitionValidationTests(unittest.TestCase):
    def test_accepts_reciprocal_inverse_definitions(self):
        relations = [{"id": "REL-A", "inverse": "REL-B", "from": ["SOURCE"], "to": ["CLAIM"]},
                     {"id": "REL-B", "inverse": "REL-A", "from": ["CLAIM"], "to": ["SOURCE"]}]
        errors = []
        validate_relation_definitions(relations, errors)
        self.assertEqual(errors, [])

    def test_rejects_non_reciprocal_inverse(self):
        relations = [{"id": "REL-A", "inverse": "REL-B", "from": ["SOURCE"], "to": ["CLAIM"]},
                     {"id": "REL-B", "inverse": "REL-C", "from": ["CLAIM"], "to": ["SOURCE"]}]
        errors = []
        validate_relation_definitions(relations, errors)
        self.assertTrue(any("does not point back" in error for error in errors))

    def test_rejects_incompatible_inverse_endpoint_types(self):
        relations = [{"id": "REL-A", "inverse": "REL-B", "from": ["SOURCE"], "to": ["CLAIM"]},
                     {"id": "REL-B", "inverse": "REL-A", "from": ["STUDY"], "to": ["SOURCE"]}]
        errors = []
        validate_relation_definitions(relations, errors)
        self.assertTrue(any("incompatible endpoint types" in error for error in errors))


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


    def test_rejects_duplicate_selected_source(self):
        batch = {**self.batch, "candidates": [
            {"candidate_id": "CANDIDATE-A", "decision": "selected", "source_id": "SOURCE-A"},
            {"candidate_id": "CANDIDATE-B", "decision": "selected", "source_id": "SOURCE-A"},
        ]}
        errors = []
        validate_batch_manifest(batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertTrue(any("selected more than once" in error for error in errors))

    def test_rejects_duplicate_reference_cycles(self):
        batch = {**self.batch, "candidates": [
            {"candidate_id": "CANDIDATE-A", "decision": "duplicate", "duplicate_of": "CANDIDATE-B"},
            {"candidate_id": "CANDIDATE-B", "decision": "duplicate", "duplicate_of": "CANDIDATE-A"},
        ]}
        errors = []
        validate_batch_manifest(batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertTrue(any("duplicate_of cycle" in error for error in errors))

    def test_closed_batch_cannot_keep_deferred_candidates(self):
        batch = {**self.batch, "status": "closed", "candidates": [
            {"candidate_id": "CANDIDATE-A", "decision": "deferred"},
        ]}
        errors = []
        validate_batch_manifest(batch, "batch.yml", {"SOURCE-A"}, errors)
        self.assertTrue(any("closed batch cannot contain deferred" in error for error in errors))


class IngestionBatchSchemaTests(unittest.TestCase):
    def test_ingestion_batch_template_matches_schema(self):
        root = Path(__file__).resolve().parents[1]
        schema = json.loads((root / "schemas" / "ingestion-batch.schema.json").read_text(encoding="utf-8"))
        template = yaml.safe_load((root / "templates" / "ingestion-batch.yml").read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
        self.assertEqual(list(validator.iter_errors(template)), [])



class ClaimExtractionSchemaTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[1]
        self.schema = json.loads((root / "schemas" / "claim.schema.json").read_text(encoding="utf-8"))
        self.validator = Draft202012Validator(self.schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
        self.claim = {
            "id": "CLAIM-EXAMPLE",
            "statement": "Un exemple de proposition vérifiable.",
            "claim_type": "descriptive",
            "status": "under_review",
            "source_verifications": [{
                "source_id": "SOURCE-EXAMPLE", "status": "source_checked",
                "locator": "Tableau 2, ligne 4",
                "extraction": {"element_type": "table_value", "value": 12.5, "unit": "%",
                               "denominator": "Ensemble des répondants", "extraction_method": "manual",
                               "extracted_at": "2026-11-18"}
            }]
        }

    def test_accepts_structured_extraction_without_requiring_migration(self):
        self.assertEqual(list(self.validator.iter_errors(self.claim)), [])

    def test_rejects_unknown_extraction_method(self):
        self.claim["source_verifications"][0]["extraction"]["extraction_method"] = "guessed"
        self.assertTrue(list(self.validator.iter_errors(self.claim)))

    def test_rejects_invalid_artifact_hash(self):
        self.claim["source_verifications"][0]["extraction"]["artifact_sha256"] = "not-a-sha256"
        self.assertTrue(list(self.validator.iter_errors(self.claim)))

    def test_real_pilot_claims_preserve_population_and_reported_values(self):
        root = Path(__file__).resolve().parents[1]
        registry = yaml.safe_load((root / "claims" / "registry.yml").read_text(encoding="utf-8"))
        claims = {claim["id"]: claim for claim in registry["claims"]}

        new_bachelors = claims["CLAIM-PARCOURSUP-2026-NEW-BACHELORS-OFFER"]
        extraction = new_bachelors["source_verifications"][0]["extraction"]
        self.assertEqual(extraction["value"], 93.7)
        self.assertIn("néo-bacheliers", extraction["population"].casefold())

        lyceens = claims["CLAIM-PARCOURSUP-2026-LYCEENS-OFFER"]
        self.assertIn("lycéens", lyceens["scope"]["population"].casefold())
        self.assertTrue(any("91,4 %" in limitation and "91,5 %" in limitation
                            for limitation in lyceens["limitations"]))
        self.assertEqual(lyceens["status"], "under_review")

        tig = claims["CLAIM-TIG-EXECUTION-DELAY-2025"]
        tig_extraction = tig["source_verifications"][0]["extraction"]
        self.assertEqual(tig_extraction["value"], 16.7)
        self.assertEqual(tig_extraction["unit"], "mois")
        self.assertIn("exécutés dans les trois ans", tig_extraction["population"])
        self.assertIn("effectif non indiqué", tig_extraction["denominator"])
        self.assertEqual(tig["status"], "under_review")

    def test_extraction_content_is_bounded_and_rejects_unknown_fields(self):
        extraction = self.claim["source_verifications"][0]["extraction"]
        extraction["extracted_content"] = "x" * 501
        self.assertTrue(list(self.validator.iter_errors(self.claim)))

        extraction.pop("extracted_content")
        extraction["invented_confidence_score"] = 0.99
        self.assertTrue(list(self.validator.iter_errors(self.claim)))

    def test_unknown_denominator_can_be_explicit_without_fabricating_count(self):
        extraction = self.claim["source_verifications"][0]["extraction"]
        extraction["denominator"] = "Effectif exact non publié dans le tableau consulté."
        self.assertEqual(list(self.validator.iter_errors(self.claim)), [])
if __name__ == "__main__":
    unittest.main()


class ControlledVocabularyValidationTests(unittest.TestCase):
    def test_accepts_current_domain_slugs_and_tag_groups(self):
        domains = [{"id": "DOMAIN-A", "slug": "public-policy"},
                   {"id": "DOMAIN-B", "slug": "labour-market"}]
        tags = [{"id": "TAG-A", "group": "method"},
                {"id": "TAG-B", "group": "evidence"},
                {"id": "TAG-C", "group": "lens"}]
        errors = []
        validate_controlled_vocabularies(domains, tags, errors)
        self.assertEqual(errors, [])

    def test_rejects_duplicate_domain_slugs_case_insensitively(self):
        domains = [{"id": "DOMAIN-A", "slug": "public-policy"},
                   {"id": "DOMAIN-B", "slug": "Public-Policy"}]
        errors = []
        validate_controlled_vocabularies(domains, [], errors)
        self.assertTrue(any("duplicate domain slug" in error for error in errors))

    def test_rejects_missing_or_malformed_domain_slugs(self):
        domains = [{"id": "DOMAIN-A"}, {"id": "DOMAIN-B", "slug": "Public Policy"}]
        errors = []
        validate_controlled_vocabularies(domains, [], errors)
        self.assertEqual(sum("invalid or missing domain slug" in e for e in errors), 2)

    def test_rejects_unknown_or_missing_tag_groups(self):
        tags = [{"id": "TAG-A", "group": "methodology"},
                {"id": "TAG-B"}]
        errors = []
        validate_controlled_vocabularies([], tags, errors)
        self.assertEqual(sum("unknown or missing tag group" in e for e in errors), 2)
