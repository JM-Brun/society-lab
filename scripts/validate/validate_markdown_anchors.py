#!/usr/bin/env python3
"""Advisory audit of GitHub-style fragments in local Markdown links."""
from __future__ import annotations
import re
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
LINK_RE = re.compile(r'!?(?:\\[[^\\]]*\\])\\(\\s*(?:<([^>]+)>|([^\\s)]+))(?:\\s+[\"\'][^)]*[\"\'])?\\s*\\)')
FENCE = chr(96)
FENCED_CODE_RE = re.compile(r'^\\s*(?:' + re.escape(FENCE) + r'{3,}|~{3,}).*?^\\s*(?:' + re.escape(FENCE) + r'{3,}|~{3,})\\s*$', re.MULTILINE | re.DOTALL)
ATX = re.compile(r'^ {0,3}#{1,6}\\s+(.+?)\\s*#*\\s*$')
INLINE_LINK = re.compile(r'!?(?:\\[([^\\]]*)\\])\\([^)]*\\)')
HTML_TAG = re.compile(r'<[^>]+>')
CODE = re.compile(re.escape(FENCE) + r'+[^' + re.escape(FENCE) + r']*' + re.escape(FENCE) + r'+')

def markdown_files(root):
    return sorted(p for p in root.rglob('*.md') if '.git' not in p.parts and not any(x.startswith('.') for x in p.relative_to(root).parts[:-1]))

def github_heading_slug(heading):
    text = CODE.sub(lambda m: m.group(0).strip(FENCE), heading)
    text = INLINE_LINK.sub(lambda m: m.group(1) or '', text)
    text = HTML_TAG.sub('', text)
    text = re.sub(r'[*_~]', '', text).strip().lower()
    chars = []
    for char in text:
        category = unicodedata.category(char)
        if char.isspace(): chars.append('-')
        elif category[0] in {'L', 'N'} or char in {'-', '_'}: chars.append(char)
    return re.sub(r'-+', '-', ''.join(chars)).strip('-')

def heading_anchors(markdown):
    counts, anchors = Counter(), set()
    for line in FENCED_CODE_RE.sub('', markdown).splitlines():
        match = ATX.match(line)
        if not match: continue
        base = github_heading_slug(match.group(1))
        if not base: continue
        suffix = counts[base]; counts[base] += 1
        anchors.add(base if suffix == 0 else f'{base}-{suffix}')
    return anchors

def local_link_fragments(markdown):
    for match in LINK_RE.finditer(FENCED_CODE_RE.sub('', markdown)):
        destination = match.group(1) or match.group(2) or ''
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc or not parsed.fragment: continue
        yield unquote(parsed.path), unquote(parsed.fragment)

def find_broken_fragments(root):
    root = root.resolve(); cache = {}; checked = 0; broken = []
    for source in markdown_files(root):
        try: content = source.read_text(encoding='utf-8')
        except (OSError, UnicodeDecodeError): continue
        for path_part, fragment in local_link_fragments(content):
            checked += 1
            target = (source.parent / path_part).resolve() if path_part else source.resolve()
            try: target.relative_to(root)
            except ValueError: continue
            if not target.is_file() or target.suffix.lower() != '.md': continue
            if target not in cache:
                try: cache[target] = heading_anchors(target.read_text(encoding='utf-8'))
                except (OSError, UnicodeDecodeError): continue
            if fragment not in cache[target]: broken.append((source.relative_to(root).as_posix(), path_part or source.name, fragment))
    return checked, broken

def main():
    files = markdown_files(ROOT); checked, broken = find_broken_fragments(ROOT)
    if broken:
        print(f'ADVISORY: {len(broken)} unresolved Markdown fragment(s) among {checked} checked links in {len(files)} Markdown file(s).')
        for source, target, fragment in broken: print(f'  - {source} -> {target}#{fragment}')
        print('Review manually: this approximation is not a CI gate.')
    else: print(f'Checked {checked} local Markdown fragment(s) in {len(files)} file(s); no unresolved fragments found.')
    return 0

if __name__ == '__main__': raise SystemExit(main())