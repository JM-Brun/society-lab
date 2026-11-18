import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts' / 'validate'))
from validate_markdown_anchors import find_broken_fragments, github_heading_slug, heading_anchors

class MarkdownAnchorValidationTests(unittest.TestCase):
    def test_slug_handles_accents_punctuation_and_spaces(self):
        self.assertEqual(github_heading_slug('État de l’école : bilan (2026)'), 'état-de-lécole-bilan-2026')
    def test_duplicate_headings_receive_numeric_suffixes(self):
        self.assertEqual(heading_anchors('# Résultat\\n# Résultat\\n'), {'résultat', 'résultat-1'})
    def test_ignores_headings_in_fenced_code(self):
        self.assertEqual(heading_anchors('# réel\\n\\n```md\\n# fictif\\n```\\n'), {'réel'})
    def test_reports_missing_fragment_and_accepts_existing_fragment(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / 'docs').mkdir()
            (root / 'docs' / 'target.md').write_text('# Présentation\\n# Résultat\\n', encoding='utf-8')
            (root / 'docs' / 'source.md').write_text('[ok](target.md#résultat) [bad](target.md#absent) [self](#présentation)\\n', encoding='utf-8')
            checked, broken = find_broken_fragments(root)
        self.assertEqual(checked, 3)
        self.assertEqual(broken, [('docs/source.md', 'target.md', 'absent')])
    def test_same_file_fragment_is_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root / 'page.md').write_text('# Intro\\n[bad](#missing)\\n', encoding='utf-8')
            checked, broken = find_broken_fragments(root)
        self.assertEqual(checked, 1)
        self.assertEqual(broken, [('page.md', 'page.md', 'missing')])

if __name__ == '__main__': unittest.main()