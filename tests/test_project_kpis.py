import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "validate"))
from calculate_project_kpis import (
    REGISTRIES,
    build_known_ids, build_node_type_index, build_report, calculate_claim_conclusion_coverage,
    calculate_connectivity_diagnostics, calculate_source_coverage, calculate_synthesis_coverage,
    inspect_relations, load_project_data, main, render_markdown,
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

    def test_unknown_relation_type_is_reported_when_taxonomy_is_supplied(self):
        valid, diagnostics = inspect_relations(
            [{**self.edge, "type": "REL-UNKNOWN"}],
            {"DOSSIER-A", "SOURCE-A"}, {"REL-INCLUDES"}
        )
        self.assertEqual(valid, [])
        self.assertEqual(diagnostics["unknown_relation_types"], ["REL-EDGE-A"])

    def test_incompatible_endpoint_types_are_reported_and_excluded(self):
        definitions = [{"id": "REL-INCLUDES", "from": ["DOSSIER"], "to": ["SOURCE"]}]
        node_types = {"DOSSIER-A": "DOSSIER", "SOURCE-A": "SOURCE"}
        valid, diagnostics = inspect_relations(
            [{**self.edge, "to": "DOSSIER-A"}],
            {"DOSSIER-A", "SOURCE-A"}, {"REL-INCLUDES"}, node_types, definitions
        )
        self.assertEqual(valid, [])
        self.assertEqual(
            diagnostics["incompatible_endpoints"],
            ["REL-EDGE-A:to:DOSSIER:REL-INCLUDES"],
        )

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

    def test_untraceable_claims_are_excluded_and_invalid_status_is_non_conclusive(self):
        result = calculate_claim_conclusion_coverage([
            {"id": "CLAIM-A", "status": "supported"},
            {"status": "supported"},
            {"id": ["CLAIM-B"], "status": "supported"},
            None,
            {"id": "CLAIM-C", "status": ["supported"]},
        ])
        self.assertEqual((result["numerator"], result["denominator"]), (1, 2))
        self.assertEqual(result["active_claim_ids"], ["CLAIM-A", "CLAIM-C"])
        self.assertEqual(result["conclusive_claim_ids"], ["CLAIM-A"])
        self.assertEqual(result["excluded_count"], 3)
        self.assertEqual(result["unknown_count"], 4)
        self.assertEqual(result["issues"], {
            "invalid_claim_entries": [
                "#2: missing or invalid claim id",
                "#3: missing or invalid claim id",
                "#4: expected a claim mapping",
            ],
            "unknown_or_missing_status": ["CLAIM-C"],
        })

    def test_no_active_claims_is_not_computable(self):
        result = calculate_claim_conclusion_coverage([{"id": "CLAIM-A", "status": "superseded"}])
        self.assertEqual(result["status"], "not_computable")
        self.assertIsNone(result["value"])

    def test_synthesis_coverage_uses_active_dossier_registry_and_allows_shared_files(self):
        with __import__("tempfile").TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "dossiers").mkdir()
            (root / "syntheses").mkdir()
            (root / "dossiers" / "a.md").write_text("# A", encoding="utf-8")
            (root / "dossiers" / "b.md").write_text("# B", encoding="utf-8")
            (root / "syntheses" / "shared.md").write_text("# Shared", encoding="utf-8")
            dossiers = [
                {"id": "DOSSIER-A", "status": "researching"},
                {"id": "DOSSIER-B", "status": "published"},
                {"id": "DOSSIER-C", "status": "archived"},
            ]
            entries = [
                {"dossier_id": "DOSSIER-A", "dossier_path": "dossiers/a.md",
                 "synthesis_id": "SYNTHESIS-SHARED", "synthesis_path": "syntheses/shared.md"},
                {"dossier_id": "DOSSIER-B", "dossier_path": "dossiers/b.md",
                 "synthesis_id": "SYNTHESIS-SHARED", "synthesis_path": "syntheses/shared.md"},
            ]
            result = calculate_synthesis_coverage(dossiers, entries, root)
        self.assertEqual((result["numerator"], result["denominator"]), (2, 2))
        self.assertEqual(result["unique_synthesis_count"], 1)
        self.assertEqual(result["excluded_count"], 1)

    def test_synthesis_coverage_reports_unknown_dossier_status_without_hiding_coverage(self):
        with __import__("tempfile").TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "dossiers").mkdir()
            (root / "syntheses").mkdir()
            (root / "dossiers" / "a.md").write_text("# A", encoding="utf-8")
            (root / "syntheses" / "a.md").write_text("# Synthesis", encoding="utf-8")
            result = calculate_synthesis_coverage(
                [{"id": "DOSSIER-A", "status": "mystery"}],
                [{"dossier_id": "DOSSIER-A", "dossier_path": "dossiers/a.md",
                  "synthesis_id": "SYNTHESIS-A", "synthesis_path": "syntheses/a.md"}],
                root,
            )
        self.assertEqual((result["numerator"], result["denominator"]), (1, 1))
        self.assertEqual(result["unknown_count"], 1)
        self.assertEqual(result["issues"], {"unknown_dossier_status": ["DOSSIER-A"]})

    def test_synthesis_coverage_flags_missing_synthesis_file(self):
        with __import__("tempfile").TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "dossiers").mkdir()
            (root / "dossiers" / "a.md").write_text("# A", encoding="utf-8")
            result = calculate_synthesis_coverage(
                [{"id": "DOSSIER-A", "status": "researching"}],
                [{"dossier_id": "DOSSIER-A", "dossier_path": "dossiers/a.md",
                  "synthesis_id": "SYNTHESIS-A", "synthesis_path": "syntheses/missing.md"}],
                root,
            )
        self.assertEqual(result["numerator"], 0)
        self.assertEqual(result["uncovered_dossier_ids"], ["DOSSIER-A"])

    def test_connectivity_diagnostics_count_invalid_edges_once(self):
        invalid = {**self.edge, "justification": ""}
        result = calculate_connectivity_diagnostics(
            [invalid], {"DOSSIER-A", "SOURCE-A"},
            {"DOSSIER-A": "DOSSIER", "SOURCE-A": "SOURCE"},
            [{"id": "REL-INCLUDES", "from": ["DOSSIER"], "to": ["SOURCE"]}],
        )
        self.assertEqual(result["excluded_invalid_relation_count"], 1)
        self.assertEqual(result["integrity_diagnostics"]["empty_justifications"], ["REL-EDGE-A"])

    def test_connectivity_diagnostics_are_descriptive_and_do_not_apply_thresholds(self):
        nodes = {
            "DOSSIER-A": "DOSSIER", "SOURCE-A": "SOURCE",
            "SOURCE-ISOLATED": "SOURCE", "CLAIM-A": "CLAIM",
        }
        definitions = [
            {"id": "REL-INCLUDES", "from": ["DOSSIER"], "to": ["SOURCE"]},
            {"id": "REL-SUPPORTS", "from": ["SOURCE"], "to": ["CLAIM"]},
        ]
        relations = [
            {**self.edge, "type": "REL-INCLUDES"},
            {"id": "REL-EDGE-B", "type": "REL-SUPPORTS", "from": "SOURCE-A",
             "to": "CLAIM-A", "justification": "La source étaye le claim."},
        ]
        result = calculate_connectivity_diagnostics(
            relations, set(nodes), nodes, definitions
        )
        self.assertEqual(result["node_types"]["SOURCE"]["node_count"], 2)
        self.assertEqual(result["node_types"]["SOURCE"]["nodes_with_relations"], 1)
        self.assertEqual(result["node_types"]["SOURCE"]["isolated_node_ids"], ["SOURCE-ISOLATED"])
        self.assertEqual(result["valid_relation_count_by_type"],
                         {"REL-INCLUDES": 1, "REL-SUPPORTS": 1})
        self.assertIn("aucun degré minimal", result["interpretation"])
        self.assertEqual(result["excluded_invalid_relation_count"], 0)

    def test_connectivity_degrees_count_unique_incident_relations(self):
        nodes = {
            "DOSSIER-A": "DOSSIER", "DOSSIER-B": "DOSSIER",
            "SOURCE-A": "SOURCE", "SOURCE-ISOLATED": "SOURCE",
        }
        definitions = [
            {"id": "REL-INCLUDES", "from": ["DOSSIER"], "to": ["SOURCE"]},
            {"id": "REL-USES", "from": ["DOSSIER"], "to": ["DOSSIER"]},
        ]
        relations = [
            {**self.edge, "type": "REL-INCLUDES"},
            {"id": "REL-EDGE-B", "type": "REL-USES", "from": "DOSSIER-A",
             "to": "DOSSIER-B", "justification": "Relation entre deux dossiers."},
            {"id": "REL-EDGE-C", "type": "REL-USES", "from": "DOSSIER-A",
             "to": "DOSSIER-A", "justification": "Boucle de contrôle."},
        ]
        result = calculate_connectivity_diagnostics(relations, set(nodes), nodes, definitions)
        dossier = result["node_types"]["DOSSIER"]
        self.assertEqual(dossier["degree_distribution"], {"1": 1, "3": 1})
        self.assertEqual((dossier["degree_min"], dossier["degree_max"]), (1, 3))
        self.assertEqual(dossier["degree_mean"], 2.0)
        self.assertEqual(dossier["relation_type_counts"], {"REL-INCLUDES": 1, "REL-USES": 2})
        self.assertEqual(dossier["connectivity_rate"], 1.0)
        source = result["node_types"]["SOURCE"]
        self.assertEqual(source["degree_distribution"], {"0": 1, "1": 1})
        self.assertEqual(source["relation_type_counts"], {"REL-INCLUDES": 1})
        self.assertEqual(source["isolated_node_ids"], ["SOURCE-ISOLATED"])

    def test_current_repository_report_is_consistent_and_fully_resolved(self):
        report = build_report(load_project_data())
        metrics = {metric["metric_id"]: metric for metric in report["metrics"]}
        source = metrics["source_to_knowledge_coverage"]
        claims = metrics["claim_conclusion_coverage"]
        syntheses = metrics["synthesis_coverage"]
        self.assertEqual(source["status"], "computed")
        self.assertEqual(source["unknown_count"], 0)
        self.assertEqual(source["issues"], {})
        self.assertEqual(len(source["covered_source_ids"]) + len(source["uncovered_source_ids"]),
                         source["denominator"])
        self.assertEqual(claims["status"], "computed")
        self.assertEqual(claims["unknown_count"], 0)
        self.assertEqual(len(claims["active_claim_ids"]), claims["denominator"])
        self.assertEqual(len(claims["conclusive_claim_ids"]), claims["numerator"])
        self.assertEqual(syntheses["status"], "computed")
        self.assertEqual(syntheses["unknown_count"], 0)
        self.assertEqual(syntheses["issues"], {})
        markdown = render_markdown(report)
        self.assertIn("Connectivité descriptive par type de nœud", markdown)
        self.assertIn("aucun degré minimal", markdown)
        self.assertEqual(len(syntheses["covered_dossier_ids"]), syntheses["numerator"])
        self.assertEqual(len(syntheses["active_dossier_ids"]), syntheses["denominator"])

    def test_revision_report_reads_committed_registries_and_file_presence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            documents = {path: {key: []} for path, key in REGISTRIES}
            documents.update({
                "knowledge/TAXONOMY.yml": {"domains": []},
                "knowledge/TERRITORIES.yml": {"territories": []},
                "knowledge/graph.yml": {"relations": []},
                "knowledge/RELATION_TYPES.yml": {"relations": []},
                "dossiers/registry.yml": {"dossiers": [{"id": "DOSSIER-A", "status": "draft"}]},
                "syntheses/registry.yml": {"dossiers": [{
                    "dossier_id": "DOSSIER-A", "dossier_path": "dossiers/a.md",
                    "synthesis_id": "SYNTHESIS-A", "synthesis_path": "syntheses/a.md",
                }]},
            })
            for relative, data in documents.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(data), encoding="utf-8")
            (root / "dossiers/a.md").touch()
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            subprocess.run(["git", "add", "."], cwd=root, check=True)
            subprocess.run([
                "git", "-c", "user.name=Test", "-c", "user.email=test@example.org",
                "-c", "commit.gpgsign=false", "commit", "-qm", "Snapshot",
            ], cwd=root, check=True)
            revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()

            (root / "syntheses/a.md").touch()
            (root / "dossiers/registry.yml").write_text('{"dossiers": []}', encoding="utf-8")
            output = root / "kpis.json"
            with patch("calculate_project_kpis.ROOT", root):
                self.assertEqual(main(["--revision", "HEAD", "--format", "json", "--output", str(output)]), 0)
                first = output.read_bytes()
                self.assertEqual(main(["--revision", revision, "--format", "json", "--output", str(output)]), 0)
                self.assertEqual(first, output.read_bytes())
                self.assertEqual(main(["--format", "json", "--output", str(output)]), 0)
                local = json.loads(output.read_bytes())

            committed = json.loads(first)
            self.assertEqual(committed["source_revision"], revision)
            self.assertNotIn("generated_at", committed)
            coverage = next(metric for metric in committed["metrics"] if metric["metric_id"] == "synthesis_coverage")
            self.assertEqual((coverage["numerator"], coverage["denominator"]), (0, 1))
            self.assertEqual(coverage["issues"]["missing_synthesis_file"], ["DOSSIER-A"])
            self.assertIn("generated_at", local)
            self.assertNotIn("source_revision", local)

    def test_node_type_index_covers_canonical_registries_and_shared_syntheses(self):
        data = {
            "registries": {
                "sources": [{"id": "SOURCE-A"}],
                "studies": [{"id": "STUDY-A"}],
                "dossiers": [{"id": "DOSSIER-A"}],
            },
            "domains": [{"id": "DOMAIN-A"}],
            "territories": [{"id": "TERRITORY-A"}],
            "synthesis_entries": [
                {"synthesis_id": "SYNTHESIS-A"}, {"synthesis_id": "SYNTHESIS-A"}
            ],
        }
        self.assertEqual(build_node_type_index(data), {
            "SOURCE-A": "SOURCE", "STUDY-A": "STUDY", "DOSSIER-A": "DOSSIER",
            "DOMAIN-A": "DOMAIN", "TERRITORY-A": "TERRITORY",
            "SYNTHESIS-A": "SYNTHESIS",
        })

    def test_synthesis_identifier_collision_with_another_registry_is_reported(self):
        data = {
            "registries": {"sources": [{"id": "SYNTHESIS-COLLISION"}]},
            "domains": [], "territories": [],
            "synthesis_entries": [{"synthesis_id": "SYNTHESIS-COLLISION"}],
        }
        known, duplicates = build_known_ids(data)
        self.assertIn("SYNTHESIS-COLLISION", known)
        self.assertEqual(duplicates, ["SYNTHESIS-COLLISION"])

    def test_known_ids_include_synthesis_registry_identifiers(self):
        data = {"registries": {"sources": [{"id": "SOURCE-A"}]},
                "domains": [{"id": "DOMAIN-A"}], "territories": [{"id": "TERRITORY-A"}],
                "synthesis_entries": [{"synthesis_id": "SYNTHESIS-A"}, {"synthesis_id": "SYNTHESIS-A"}]}
        known, duplicates = build_known_ids(data)
        self.assertEqual(known, {"SOURCE-A", "DOMAIN-A", "TERRITORY-A", "SYNTHESIS-A"})
        self.assertEqual(duplicates, [])

if __name__ == "__main__":
    unittest.main()
