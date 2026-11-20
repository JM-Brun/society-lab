import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from trace_knowledge_impact import (
    build_event_impact_report, build_git_impact_report, build_impact_report,
    compare_sources, render_event_markdown, render_markdown,
)


class GitSourceImpactTests(unittest.TestCase):
    def test_registry_order_and_yaml_key_order_do_not_count_as_source_changes(self):
        before = [{"id": "SOURCE-A", "authors": ["A", "B"]}, {"id": "SOURCE-B"}]
        after = [{"id": "SOURCE-B"}, {"authors": ["A", "B"], "id": "SOURCE-A"}]
        self.assertEqual(compare_sources(before, after), [])
        after[1]["authors"].reverse()
        self.assertEqual(compare_sources(before, after), [
            {"source_id": "SOURCE-A", "change": "modified", "changed_fields": ["authors"]},
        ])

    def test_uses_both_commits_when_sources_or_their_links_are_removed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            def git(*args):
                return subprocess.check_output(["git", *args], cwd=root, encoding="utf-8").strip()

            def write(relative, data):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(yaml.safe_dump(data), encoding="utf-8")

            def commit():
                git("add", ".")
                git("-c", "user.name=Test", "-c", "user.email=test@example.org", "commit", "-qm", "Snapshot")
                return git("rev-parse", "HEAD")

            git("init", "-q")
            write("knowledge/graph.yml", {"relations": []})
            write("syntheses/registry.yml", {"dossiers": []})
            write("sources/registry.yml", {"sources": [
                {"id": "SOURCE-RETIRED", "title": "Retired source"},
                {"id": "SOURCE-MODIFIED", "title": "Previous version"},
            ]})
            write("research/studies/registry.yml", {"studies": [
                {"id": "STUDY-OLD", "source_ids": ["SOURCE-RETIRED", "SOURCE-MODIFIED"]},
            ]})
            base = commit()
            write("sources/registry.yml", {"sources": [
                {"id": "SOURCE-MODIFIED", "title": "Revised version"},
                {"id": "SOURCE-NEW", "title": "New source"},
            ]})
            write("research/studies/registry.yml", {"studies": [
                {"id": "STUDY-NEW", "source_ids": ["SOURCE-NEW", "SOURCE-MODIFIED"]},
            ]})
            event = {
                "id": "EVENT-SOURCE-REPLACEMENT", "kind": "new_version",
                "source_id": "SOURCE-MODIFIED", "replacement_source_id": "SOURCE-NEW",
                "baseline_revision": base, "recorded_on": "2026-11-20",
                "evidence": {"url": "https://example.org", "locator": "Version history"},
                "summary": "Updated release identified.",
                "decisions": [
                    {"target_id": "SOURCE-MODIFIED", "status": "corrected",
                     "reason": "Notice recorded.", "reviewed_on": "2026-11-20"},
                    {"target_id": "DOSSIER-MANUAL", "status": "needs_review",
                     "reason": "Documentary reference mentioned in prose.", "reviewed_on": "2026-11-20"},
                ],
            }
            write("sources/lifecycle.yml", {"events": [event]})
            head = commit()
            write("sources/registry.yml", {"sources": []})

            report = build_git_impact_report(root, base, "HEAD")
            self.assertEqual((report["base_revision"], report["revision"]), (base, head))
            modified, added, removed = report["sources"]
            self.assertEqual([x["change"] for x in report["sources"]], ["modified", "added", "removed"])
            self.assertEqual(modified["changed_fields"], ["title"])
            self.assertEqual(modified["impact_before"]["records"]["STUDY"][0]["id"], "STUDY-OLD")
            self.assertEqual(modified["impact_after"]["records"]["STUDY"][0]["id"], "STUDY-NEW")
            self.assertNotIn("impact_before", added)
            self.assertEqual(removed["impact_before"]["records"]["STUDY"][0]["id"], "STUDY-OLD")
            self.assertNotIn("impact_after", removed)

            review = build_event_impact_report(root, event["id"], head)
            self.assertEqual(review["revision"], head)
            self.assertEqual(review["impacts"]["replacement"]["source_id"], "SOURCE-NEW")
            self.assertEqual(review["targets_without_decision"], ["SOURCE-NEW", "STUDY-NEW", "STUDY-OLD"])
            self.assertEqual(review["decisions_outside_detected_impact"], ["DOSSIER-MANUAL"])
            self.assertIn("STUDY-OLD", render_event_markdown(review))
            self.assertIn("needs_review", render_event_markdown(review))


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

    def test_real_parcoursup_2026_ministry_source_traces_to_dossier_and_synthesis(self):
        from trace_knowledge_impact import ROOT, load_repository

        registries, graph, syntheses = load_repository(ROOT)
        report = build_impact_report(
            registries, graph, syntheses,
            "SOURCE-PARCOURSUP-BILAN-2026",
        )
        studies = {item["id"] for item in report["records"].get("STUDY", [])}
        datasets = {item["id"] for item in report["records"].get("DATASET", [])}
        claims = {item["id"] for item in report["records"].get("CLAIM", [])}
        dossiers = {item["id"] for item in report["records"].get("DOSSIER", [])}

        self.assertIn("STUDY-PARCOURSUP-ADMISSIONS-2026", studies)
        self.assertIn("DATASET-PARCOURSUP-2026-INDICATORS", datasets)
        self.assertIn("CLAIM-PARCOURSUP-2026-APPLICANTS", claims)
        self.assertIn("CLAIM-PARCOURSUP-2026-LYCEENS-OFFER", claims)
        self.assertIn("DOSSIER-PARCOURSUP-EDUCATION-EQUITY", dossiers)
        self.assertTrue(any(
            item["dossier_id"] == "DOSSIER-PARCOURSUP-EDUCATION-EQUITY"
            and item["synthesis_path"] == "syntheses/parcoursup-education.md"
            for item in report["syntheses"]
        ))

    def test_real_parcoursup_2026_sies_source_traces_through_study(self):
        from trace_knowledge_impact import ROOT, load_repository

        registries, graph, syntheses = load_repository(ROOT)
        report = build_impact_report(
            registries, graph, syntheses,
            "SOURCE-SIES-PARCOURSUP-2026-ADMISSIONS",
        )
        studies = {item["id"] for item in report["records"].get("STUDY", [])}
        datasets = {item["id"] for item in report["records"].get("DATASET", [])}
        claims = {item["id"] for item in report["records"].get("CLAIM", [])}
        dossiers = {item["id"] for item in report["records"].get("DOSSIER", [])}

        self.assertIn("STUDY-PARCOURSUP-ADMISSIONS-2026", studies)
        self.assertIn("DATASET-PARCOURSUP-2026-INDICATORS", datasets)
        self.assertIn("CLAIM-PARCOURSUP-2026-NEW-BACHELORS-OFFER", claims)
        self.assertIn("DOSSIER-PARCOURSUP-EDUCATION-EQUITY", dossiers)
        self.assertTrue(any(
            item["dossier_id"] == "DOSSIER-PARCOURSUP-EDUCATION-EQUITY"
            and item["synthesis_path"] == "syntheses/parcoursup-education.md"
            for item in report["syntheses"]
        ))

    def test_real_ademe_season2_source_does_not_infer_dossier_from_graph_edge(self):
        from trace_knowledge_impact import ROOT, load_repository

        registries, graph, syntheses = load_repository(ROOT)
        source_id = "SOURCE-ADEME-TRANSITIONS2050-SEASON2-OPEN-DATA"
        report = build_impact_report(registries, graph, syntheses, source_id)

        self.assertEqual(report["source_id"], source_id)
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
