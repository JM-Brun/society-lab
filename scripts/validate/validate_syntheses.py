#!/usr/bin/env python3
"""Ensure every top-level research dossier has a complete, linked synthesis."""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
DOSSIER_REGISTRY = ROOT / "dossiers" / "registry.yml"
SYNTHESIS_REGISTRY = ROOT / "syntheses" / "registry.yml"
ALLOWED_STATUS = {"draft", "in_review", "provisional", "validated", "superseded"}
ALLOWED_CONFIDENCE = {"low", "moderate", "high"}
REQUIRED_HEADINGS = [
    (r"^## 1\. Synthèse exécutive$", "synthèse exécutive"),
    (r"^## 2\. Question et périmètre$", "question et périmètre"),
    (r"^## 3\. Principaux constats$", "principaux constats"),
    (r"^## 4\. Ce que montrent les preuves$", "analyse des preuves"),
    (r"^## 5\. Débat contradictoire", "débat contradictoire"),
    (r"^## 6\. Incertitudes", "incertitudes et limites"),
    (r"^## 7\. Conclusion", "conclusion raisonnée"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def load_yaml(path: Path) -> dict:
    if not path.is_file():
        raise ValueError(f"missing file: {path.relative_to(ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"expected YAML mapping in {path.relative_to(ROOT)}")
    return data


def read_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\\n"):
        raise ValueError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise ValueError(f"{path.relative_to(ROOT)}: malformed YAML frontmatter")
    metadata = yaml.safe_load(parts[1])
    if not isinstance(metadata, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: frontmatter must be a mapping")
    return metadata, parts[2]


def main() -> int:
    errors: list[str] = []
    try:
        dossiers = load_yaml(DOSSIER_REGISTRY).get("dossiers", [])
        syntheses = load_yaml(SYNTHESIS_REGISTRY).get("dossiers", [])
    except (ValueError, yaml.YAMLError) as exc:
        fail(str(exc))
        return 1

    dossier_by_id = {item.get("id"): item for item in dossiers if isinstance(item, dict)}
    synthesis_by_id = {item.get("dossier_id"): item for item in syntheses if isinstance(item, dict)}

    missing = sorted(set(dossier_by_id) - set(synthesis_by_id))
    stale = sorted(set(synthesis_by_id) - set(dossier_by_id))
    if missing:
        errors.append("no synthesis mapping for dossier(s): " + ", ".join(missing))
    if stale:
        errors.append("synthesis mapping references unknown dossier(s): " + ", ".join(stale))

    for dossier_id, entry in synthesis_by_id.items():
        dossier = dossier_by_id.get(dossier_id)
        if dossier is None:
            continue
        dossier_path = ROOT / entry.get("dossier_path", "")
        synthesis_path = ROOT / entry.get("synthesis_path", "")
        if not dossier_path.is_file():
            errors.append(f"{dossier_id}: dossier file missing: {entry.get('dossier_path')}")
            continue
        if not synthesis_path.is_file():
            errors.append(f"{dossier_id}: synthesis file missing: {entry.get('synthesis_path')}")
            continue
        try:
            metadata, body = read_frontmatter(synthesis_path)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
            continue

        if metadata.get("id") != entry.get("synthesis_id"):
            errors.append(f"{entry.get('synthesis_path')}: synthesis id does not match registry")
        for field in ("title", "domain", "last_reviewed", "related_dossiers"):
            if not metadata.get(field):
                errors.append(f"{entry.get('synthesis_path')}: missing required metadata '{field}'")
        if metadata.get("status") not in ALLOWED_STATUS:
            errors.append(f"{entry.get('synthesis_path')}: invalid or missing status")
        if metadata.get("confidence") not in ALLOWED_CONFIDENCE:
            errors.append(f"{entry.get('synthesis_path')}: invalid or missing confidence")
        if entry.get("dossier_path") not in (metadata.get("related_dossiers") or []):
            errors.append(f"{entry.get('synthesis_path')}: related_dossiers must include {entry.get('dossier_path')}")

        for pattern, label in REQUIRED_HEADINGS:
            if not re.search(pattern, body, flags=re.MULTILINE):
                errors.append(f"{entry.get('synthesis_path')}: missing required section: {label}")

    if errors:
        for error in errors:
            fail(error)
        return 1

    print(f"Validated {len(dossier_by_id)} main dossier(s): each has a linked synthesis with required metadata and sections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
