#!/usr/bin/env python3
"""Report broken local links in Markdown files without failing CI by default."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(
    r"!?(?:\[[^\]]*\])\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+[\"'][^)]*[\"'])?\s*\)"
)
FENCED_CODE_RE = re.compile(r"^\s*(```+|~~~+).*?^\s*\1\s*$", re.MULTILINE | re.DOTALL)


def markdown_files(root: Path) -> list[Path]:
    """Return tracked-tree candidates; generated and hidden metadata are excluded."""
    return sorted(
        path for path in root.rglob("*.md")
        if ".git" not in path.parts and not any(part.startswith(".") for part in path.relative_to(root).parts[:-1])
    )


def local_link_targets(markdown: str):
    """Yield link destinations, excluding fenced code and external/anchor-only links."""
    text = FENCED_CODE_RE.sub("", markdown)
    for match in LINK_RE.finditer(text):
        destination = match.group(1) or match.group(2) or ""
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        yield unquote(parsed.path)


def find_broken_local_links(root: Path) -> tuple[int, list[tuple[str, str]]]:
    """Return the number of local links checked and missing/escaping targets."""
    checked = 0
    broken: list[tuple[str, str]] = []
    root = root.resolve()
    for source in markdown_files(root):
        try:
            content = source.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for destination in local_link_targets(content):
            checked += 1
            target = (source.parent / destination).resolve()
            try:
                target.relative_to(root)
            except ValueError:
                broken.append((source.relative_to(root).as_posix(), destination))
                continue
            if not target.exists():
                broken.append((source.relative_to(root).as_posix(), destination))
    return checked, broken


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true", help="return a failure when broken links are found")
    args = parser.parse_args()

    files = markdown_files(ROOT)
    checked, broken = find_broken_local_links(ROOT)
    if broken:
        print(
            f"WARNING: {len(broken)} broken or escaping local Markdown link(s) "
            f"among {checked} checked links in {len(files)} Markdown file(s)."
        )
        for source, destination in broken:
            print(f"  - {source} -> {destination}")
        return 1 if args.strict else 0

    print(f"Checked {checked} local Markdown link(s) in {len(files)} file(s); no broken targets found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
