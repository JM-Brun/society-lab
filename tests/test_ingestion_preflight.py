import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "audit"))

from check_ingestion_candidates import build_report, load_batch, normalize_doi


class IngestionPreflightTests(unittest.TestCase):
    def test_doi_sources_are_recognized_without_rewriting_other_url_keys(self):
        sources = [
            {"id": "SOURCE-B", "url": "http://dx.doi.org/10.1000/AbC?tracking=1"},
            {"id": "SOURCE-A", "doi": " DOI:10.1000/ABC ", "url": "https://example.org/report?v=1"},
        ]
        candidates = [
            {"candidate_id": "CANDIDATE-A", "decision": "deferred", "external_identifier": "https://doi.org/10.1000/%41bc",
             "canonical_url": "https://example.org/report?v=2"},
            {"candidate_id": "CANDIDATE-B", "decision": "deferred", "canonical_url": "https://example.org/report?v=2",
             "external_identifier": "ISBN:9781234567897"},
            {"candidate_id": "CANDIDATE-C", "decision": "selected", "source_id": "SOURCE-B"},
        ]
        report = build_report(sources, {"batch_id": "BATCH-A", "candidates": candidates})
        self.assertEqual(report["decision_counts"], {"deferred": 2, "selected": 1})
        self.assertEqual(report["registry_collisions"], [
            {"kind": "doi", "value": "10.1000/abc", "source_ids": ["SOURCE-A", "SOURCE-B"]},
        ])
        by_kind = {match["kind"]: match for match in report["batch_matches"]}
        self.assertEqual(by_kind["doi"]["candidate_ids"], ["CANDIDATE-A"])
        self.assertEqual(by_kind["source_id"]["source_ids"], ["SOURCE-B"])
        self.assertEqual(by_kind["url"]["source_ids"], [])
        self.assertEqual(by_kind["url"]["candidate_ids"], ["CANDIDATE-A", "CANDIDATE-B"])
        self.assertEqual(normalize_doi("", "https://doi.org.example.org/10.1000/abc"), "")
        self.assertEqual(report, build_report(list(reversed(sources)), {
            "batch_id": "BATCH-A", "candidates": list(reversed(candidates)),
        }))

    def test_local_artifact_is_hashed_and_checked_against_declared_digest(self):
        with tempfile.TemporaryDirectory() as directory:
            batch_path = Path(directory) / "batch.yml"
            artifact = Path(directory) / "source.txt"
            artifact.write_bytes(b"source bytes\n")
            digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
            template = ROOT / "templates" / "ingestion-batch.yml"
            batch = yaml.safe_load(template.read_text(encoding="utf-8"))
            candidate = batch["candidates"][0]
            batch_path.write_text(yaml.safe_dump(batch), encoding="utf-8")
            artifacts = [[candidate["candidate_id"], str(artifact)]]
            sources = [{"id": "SOURCE-A", "artifact_sha256": digest.upper()}]
            report = build_report(sources, load_batch(batch_path, artifacts, {"SOURCE-A"}))
            self.assertEqual(report["batch_matches"], [
                {"kind": "artifact_sha256", "value": digest, "source_ids": ["SOURCE-A"],
                 "candidate_ids": [candidate["candidate_id"]]},
            ])
            self.assertNotIn("artifact_sha256", yaml.safe_load(batch_path.read_text())["candidates"][0])

            candidate["artifact_sha256"] = "0" * 64
            batch_path.write_text(yaml.safe_dump(batch), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "SHA-256 differs"):
                load_batch(batch_path, artifacts, {"SOURCE-A"})
            candidate["artifact_sha256"] = digest + "\n"
            batch_path.write_text(yaml.safe_dump(batch), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "invalid batch field candidates.0.artifact_sha256"):
                load_batch(batch_path, [], {"SOURCE-A"})

    def test_manifest_rejects_an_unresolved_selected_source(self):
        template = ROOT / "templates" / "ingestion-batch.yml"
        batch = yaml.safe_load(template.read_text(encoding="utf-8"))
        batch["candidates"][0].update(decision="selected", source_id="SOURCE-MISSING")
        with tempfile.TemporaryDirectory() as directory:
            batch_path = Path(directory) / "batch.yml"
            batch_path.write_text(yaml.safe_dump(batch), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unresolved source_id SOURCE-MISSING"):
                load_batch(batch_path, [], {"SOURCE-A"})


if __name__ == "__main__":
    unittest.main()
