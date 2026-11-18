import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "validate"))
from validate_markdown_links import find_broken_local_links, local_link_targets


class MarkdownLinkValidationTests(unittest.TestCase):
    def test_extracts_relative_links_but_skips_external_and_anchor_links(self):
        content = """[file](../docs/report.md#section) [web](https://example.org/a.md) [anchor](#top)
"""
        self.assertEqual(list(local_link_targets(content)), ["../docs/report.md"])

    def test_ignores_links_inside_fenced_code_blocks(self):
        content = """[real](exists.md)

```markdown
[example](missing.md)
```
"""
        self.assertEqual(list(local_link_targets(content)), ["exists.md"])

    def test_reports_missing_relative_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "source.md").write_text("[ok](target.md) [bad](missing.md)\n", encoding="utf-8")
            (root / "docs" / "target.md").write_text("# target\n", encoding="utf-8")
            checked, broken = find_broken_local_links(root)

        self.assertEqual(checked, 2)
        self.assertEqual(broken, [("docs/source.md", "missing.md")])

    def test_reports_paths_that_escape_repository_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "source.md").write_text("[bad](../../../outside.md)\n", encoding="utf-8")
            checked, broken = find_broken_local_links(root)

        self.assertEqual(checked, 1)
        self.assertEqual(broken, [("docs/source.md", "../../../outside.md")])


if __name__ == "__main__":
    unittest.main()
