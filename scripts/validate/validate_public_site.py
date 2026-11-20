"""Verify the scope and local links of the Quarto output before upload."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

SITE = Path(__file__).resolve().parents[2] / "site"
OUTPUT = SITE / "_site"
PUBLIC_METADATA = {"robots.txt", "search.json", "sitemap.xml"}
LIBRARY_SUFFIXES = {".css", ".js", ".map", ".woff", ".woff2"}


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.references = []
        self.feed(path.read_text(encoding="utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        self.references.extend(
            value for key, value in attrs if key in {"href", "src"} and value
        )


def main():
    config = yaml.safe_load((SITE / "_quarto.yml").read_text(encoding="utf-8"))
    targets = [Path(target) for target in config["project"]["render"]]
    index = Path("index.qmd")
    invalid = [
        target for target in set(targets) - {index}
        if target.parent != Path("syntheses") or target.suffix != ".qmd"
        or "*" in target.name or not (SITE / target).is_file()
    ]
    if index not in targets or invalid:
        raise SystemExit(f"Render targets must list index.qmd and individual syntheses: {invalid}")

    expected = {target.with_suffix(".html") for target in targets}
    files = {path.relative_to(OUTPUT) for path in OUTPUT.rglob("*") if path.is_file()}
    missing = expected - files
    unexpected = {
        path for path in files - expected
        if path.as_posix() not in PUBLIC_METADATA
        and not (path.parts[0] == "site_libs" and path.suffix in LIBRARY_SUFFIXES)
    }
    symlinks = {path.relative_to(OUTPUT) for path in OUTPUT.rglob("*") if path.is_symlink()}
    errors = [f"Missing page: {path}" for path in sorted(missing)]
    errors += [f"Unexpected public file: {path}" for path in sorted(unexpected | symlinks)]

    base = urlsplit(config["website"]["site-url"]).path
    for path in sorted(expected & files):
        for reference in Page(OUTPUT / path).references:
            url = urlsplit(reference)
            if url.scheme or url.netloc or not url.path:
                continue
            target = unquote(url.path)
            if target.startswith(base):
                resolved = (OUTPUT / target.removeprefix(base)).resolve()
            else:
                resolved = (OUTPUT / path.parent / target).resolve()
            if resolved.is_dir():
                resolved /= "index.html"
            if not resolved.is_relative_to(OUTPUT) or not resolved.is_file():
                errors.append(f"Unresolved public link in {path}: {reference}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Public site verified: {len(expected)} HTML pages and their local assets.")


if __name__ == "__main__":
    main()
