import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "validate"))
from check_synthesis_freshness import classify_source, read_metadata


class SynthesisFreshnessTests(unittest.TestCase):
    def test_source_modified_after_review_requires_review(self):
        self.assertEqual(
            classify_source(date(2026, 11, 10), date(2026, 11, 11)),
            "À RÉVISER",
        )

    def test_source_not_modified_after_review_has_no_alert(self):
        self.assertEqual(
            classify_source(date(2026, 11, 10), date(2026, 11, 10)),
            "AUCUNE ALERTE",
        )
        self.assertEqual(
            classify_source(date(2026, 11, 10), date(2026, 11, 9)),
            "AUCUNE ALERTE",
        )

    def test_missing_git_history_is_unknown(self):
        self.assertEqual(classify_source(date(2026, 11, 10), None), "INCONNU")

    def test_reads_front_matter_metadata(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthesis.md"
            path.write_text(
                '---\nid: "SYNTHESIS-TEST"\nlast_reviewed: "2026-11-10"\n'
                'related_dossiers: ["dossiers/example.md"]\n---\n# Test\n',
                encoding="utf-8",
            )
            metadata = read_metadata(path)
        self.assertEqual(metadata["id"], "SYNTHESIS-TEST")
        self.assertEqual(metadata["related_dossiers"], ["dossiers/example.md"])

    def test_rejects_missing_front_matter(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthesis.md"
            path.write_text("# No metadata\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_metadata(path)


if __name__ == "__main__":
    unittest.main()
