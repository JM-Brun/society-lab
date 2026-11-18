from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "validate"))

from validate_syntheses import find_unreferenced_markdown_files


class SynthesisFileCoverageTests(unittest.TestCase):
    def test_reports_unreferenced_markdown_without_treating_it_as_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "dossiers").mkdir()
            (root / "dossiers" / "main.md").write_text("# Main\n", encoding="utf-8")
            (root / "dossiers" / "working-note.md").write_text("# Note\n", encoding="utf-8")
            (root / "dossiers" / "README.md").write_text("# Readme\n", encoding="utf-8")

            result = find_unreferenced_markdown_files(
                root, "dossiers", {"dossiers/main.md"}
            )

        self.assertEqual(result, ["dossiers/working-note.md"])

    def test_missing_directory_is_an_empty_inventory(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = find_unreferenced_markdown_files(
                Path(tmp), "dossiers", set()
            )

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
