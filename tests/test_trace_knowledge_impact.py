import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from trace_knowledge_impact import build_impact_report, render_markdown


class SourceImpactTracingTests(unittest.TestCase):
    def setUp(self):
        self.registries = {
            "SOURCE": [{"id": "SOURCE-A", "title": "Primary source"}],
            "STUDY": [{"id": "STUDY-A", "title": "Study A", "source_ids": ["SOURCE-A"]}],
            "DATASET": [{"id": "DATASET-A", "title": "Dataset A", "source_ids": ["SOURCE-A"]}],
            "CLAIM": [
                {"id": "CLAIM-A", "statement": "Claim A", "source_verifications": [{"source_id": "SOURCE-A"}]},
                {"id": "CLAIM-B", "statement": "Claim B", "study_ids": ["STUDY-A"], "dataset_ids": ["DATASET-A"]},
            ],
            "HYPOTHESIS": [{"id": "HYPOTHESIS-A", "statement": "Hypothesis A", "supporting_study_ids": ["STUDY-A"]}],
            "DOSSIER": [{
                "id": "DOSSIER-A", "title": "Dossier A", "claim_ids": ["CLAIM-B"],
                "study_ids": [], "hypothesis_ids": ["HYPOTHESIS-A"], "concept_ids": [],
            }],
            "CONCEPT": [],
        }
        self.graph = [
            {"id": "REL-A", "type": "REL-SUPPORTS", "from": "STUDY-A", "to": "CLAIM-B", "justification": "Evidence link"},
            {"id": "REL-DOMAIN", "type": "REL-ABOUT", "from": "SOURCE-A", "to": "DOMAIN-ECONOMY", "justification": "Domain link"},
        ]
        self.syntheses = [{
            "dossier_id": "DOSSIER-A", "synthesis_id": "SYNTHESIS-A",
            "synthesis_path": "syntheses/example.md",
        }]

    def test_traces_explicit_dependencies_to_synthesis(self):
        report = build_impact_report(self.registries, self.graph, self.syntheses, "SOURCE-A")
        self.assertEqual({x["id"] for x in report["records"]["STUDY"]}, {"STUDY-A"})
        self.assertEqual({x["id"] for x in report["records"]["DATASET"]}, {"DATASET-A"})
        self.assertEqual({x["id"] for x in report["records"]["CLAIM"]}, {"CLAIM-A", "CLAIM-B"})
        self.assertEqual({x["id"] for x in report["records"]["HYPOTHESIS"]}, {"HYPOTHESIS-A"})
        self.assertEqual({x["id"] for x in report["records"]["DOSSIER"]}, {"DOSSIER-A"})
        self.assertEqual(report["syntheses"][0]["synthesis_id"], "SYNTHESIS-A")

    def test_source_verifications_are_only_source_dependencies_for_claims(self):
        registries = {
            **self.registries,
            "STUDY": [{
                "id": "STUDY-A", "title": "Study A",
                "source_verifications": [{"source_id": "SOURCE-A"}],
            }],
            "DATASET": [],
        }
        report = build_impact_report(registries, self.graph, self.syntheses, "SOURCE-A")

        # source_verifications is a claim-level field, not a generic reference
        # accepted on every object type.
        self.assertNotIn("STUDY", report["records"])
        self.assertEqual(
            {item["id"] for item in report["records"]["CLAIM"]},
            {"CLAIM-A"},
        )

    def test_traces_impact_to_mechanisms_and_forecasts_by_typed_references(self):
        registries = {
            **self.registries,
            "MECHANISM": [{
                "id": "MECHANISM-A",
                "label": "Mechanism A",
                "supporting_study_ids": ["STUDY-A"],
                "challenging_study_ids": [],
                "claim_ids": ["CLAIM-B"],
            }],
            "FORECAST": [{
                "id": "FORECAST-A",
                "question": "Will the defined event occur?",
                "claim_ids": ["CLAIM-A"],
            }],
        }
        report = build_impact_report(registries, self.graph, self.syntheses, "SOURCE-A")

        self.assertEqual(
            {item["id"] for item in report["records"]["MECHANISM"]},
            {"MECHANISM-A"},
        )
        self.assertEqual(
            {item["id"] for item in report["records"]["FORECAST"]},
            {"FORECAST-A"},
        )
        rendered = render_markdown(report)
        self.assertIn("Mécanismes explicatifs à revoir", rendered)
        self.assertIn("Prévisions dépendantes à réexaminer", rendered)

    def test_graph_edges_are_context_not_transitive_dependencies(self):
        report = build_impact_report(self.registries, self.graph, self.syntheses, "SOURCE-A")
        self.assertEqual({x["id"] for x in report["graph_edges"]}, {"REL-A", "REL-DOMAIN"})
        self.assertNotIn("DOMAIN", report["records"])

    def test_unknown_source_fails_clearly(self):
        with self.assertRaisesRegex(ValueError, "Unknown source id"):
            build_impact_report(self.registries, self.graph, self.syntheses, "SOURCE-MISSING")


    def test_real_tig_source_traces_to_claim_dossier_and_synthesis(self):
        from trace_knowledge_impact import ROOT, load_repository

        registries, graph, syntheses = load_repository(ROOT)
        report = build_impact_report(
            registries, graph, syntheses,
            "SOURCE-COUR-DES-COMPTES-PEINES-ALTERNATIVES-2025",
        )
        claims = {item["id"] for item in report["records"].get("CLAIM", [])}
        dossiers = {item["id"] for item in report["records"].get("DOSSIER", [])}
        self.assertIn("CLAIM-TIG-EXECUTION-DELAY-2025", claims)
        self.assertIn("DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE", dossiers)
        self.assertTrue(any(
            item["dossier_id"] == "DOSSIER-TIG-EFFECTIVENESS-AND-UNDERUSE"
            and item["synthesis_path"] == "syntheses/tig-france.md"
            for item in report["syntheses"]
        ))

    def test_real_ademe_season2_source_does_not_infer_dossier_from_graph_edge(self):
        from trace_knowledge_impact import ROOT, load_repository

        registries, graph, syntheses = load_repository(ROOT)
        source_id = "SOURCE-ADEME-TRANSITIONS2050-SEASON2-OPEN-DATA"
        report = build_impact_report(registries, graph, syntheses, source_id)

        self.assertEqual(report["source_id"], source_id)
        # The dossier/source relation exists in the graph, but is contextual:
        # it must not be promoted to an explicit epistemic dependency.
        self.assertNotIn("DOSSIER", report["records"])
        self.assertEqual(report["syntheses"], [])
        self.assertIn(
            "REL-QUANT-DOSSIER-INCLUDES-ADEME-SEASON2",
            {edge["id"] for edge in report["graph_edges"]},
        )

    def test_markdown_warns_against_automatic_invalidation(self):
        report = build_impact_report(self.registries, self.graph, self.syntheses, "SOURCE-A")
        rendered = render_markdown(report)
        self.assertIn("Décision humaine requise", rendered)
        self.assertIn("pas une invalidité automatique", rendered)


if __name__ == "__main__":
    unittest.main()
