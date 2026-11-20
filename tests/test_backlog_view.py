import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.report import generate_backlog_view as backlog
from scripts.report.generate_backlog_view import build_rows, render_markdown

class BacklogViewTests(unittest.TestCase):
    def setUp(self):
        self.mapping={"issues":[{"issue":7,"kind":"research","dossier_ids":["D1"],"depends_on":[8]},{"issue":8,"kind":"meta","dossier_ids":[],"depends_on":[]}]}
        self.dossiers={"dossiers":[{"id":"D1","title":"Dossier test","domain_ids":["DOMAIN-A","DOMAIN-B"]}]}
        self.issues=[{"number":7,"title":"Sujet","html_url":"https://example.test/7","labels":[{"name":"priority:high"},{"name":"research"}]},{"number":8,"title":"Gouvernance","html_url":"https://example.test/8","labels":[{"name":"priority:medium"},{"name":"meta"},{"name":"documentation"}]},{"number":9,"title":"Non mappée","html_url":"https://example.test/9","labels":[{"name":"priority:low"}]}]
    def test_domains_derive_from_linked_dossiers(self):
        row=next(item for item in build_rows(self.issues,self.mapping,self.dossiers) if item["number"]==7)
        self.assertEqual(row["domain_ids"],["DOMAIN-A","DOMAIN-B"])
    def test_unmapped_issue_is_not_guessed(self):
        row=next(item for item in build_rows(self.issues,self.mapping,self.dossiers) if item["number"]==9)
        self.assertEqual(row["kind"],"unmapped"); self.assertEqual(row["domain_ids"],[]); self.assertFalse(row["mapping_valid"])
    def test_invalid_priority_is_flagged(self):
        issue=dict(self.issues[0],labels=[{"name":"priority:high"},{"name":"priority:low"}])
        row=build_rows([issue],self.mapping,self.dossiers)[0]
        self.assertFalse(row["priority_valid"]); self.assertEqual(row["priority"],"unclassified")
    def test_rendering_includes_domain_and_dependencies(self):
        output=render_markdown(build_rows(self.issues,self.mapping,self.dossiers),"2026-11-18T12:00+00:00")
        self.assertIn("DOMAIN-A, DOMAIN-B",output); self.assertIn("#8",output); self.assertIn("À qualifier",output)

    def test_captured_report_replays_without_github_or_git(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            snapshot_path = root / "snapshot.json"
            live_path = root / "live.md"
            replay_path = root / "replay.md"
            issues = [dict(issue, body="Unused issue body") for issue in reversed(self.issues)]
            with (
                patch.dict(os.environ, {"BACKLOG_OUTPUT": str(live_path), "GITHUB_TOKEN": "fixture"}, clear=True),
                patch.object(backlog, "read_git", side_effect=["fixture-commit\n", json.dumps(self.mapping), json.dumps(self.dossiers)]) as git,
                patch.object(backlog, "fetch_open_issues", return_value=issues),
            ):
                self.assertEqual(backlog.main(["--snapshot-output", str(snapshot_path)]), 0)
                git.assert_any_call("show", f"fixture-commit:{backlog.MAPPING}")
                git.assert_any_call("show", f"fixture-commit:{backlog.DOSSIERS}")

            snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
            self.assertEqual(snapshot["source_revision"], "fixture-commit")
            self.assertEqual([issue["number"] for issue in snapshot["issues"]], [7, 8, 9])
            self.assertEqual(set(snapshot["issues"][0]), {"number", "title", "html_url", "labels"})
            self.assertEqual(set(snapshot["dossiers"]["dossiers"][0]), {"id", "domain_ids"})
            with (
                patch.dict(os.environ, {"BACKLOG_OUTPUT": str(replay_path)}, clear=True),
                patch.object(backlog, "fetch_open_issues") as api,
                patch.object(backlog, "read_git") as git,
                patch.object(backlog, "load_yaml") as yaml,
            ):
                self.assertEqual(backlog.main(["--snapshot-input", str(snapshot_path)]), 0)
                api.assert_not_called()
                git.assert_not_called()
                yaml.assert_not_called()
            self.assertEqual(live_path.read_bytes(), replay_path.read_bytes())
            self.assertIn("DOMAIN-A, DOMAIN-B", replay_path.read_text(encoding="utf-8"))

if __name__=="__main__": unittest.main()
