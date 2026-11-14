#!/usr/bin/env python3
"""Advisory freshness report for every dossier linked to a subject synthesis."""
from __future__ import annotations

import os
import subprocess
import sys
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "syntheses" / "registry.yml"


def latest_commit_date(relative_path: str) -> date | None:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", relative_path],
        cwd=ROOT, text=True, capture_output=True, check=True,
    )
    value = result.stdout.strip()
    return date.fromisoformat(value) if value else None


def classify_source(reviewed: date, source_date: date | None) -> str:
    if source_date is None:
        return "INCONNU"
    return "À RÉVISER" if source_date > reviewed else "AUCUNE ALERTE"


def read_metadata(synthesis_file: Path) -> dict:
    content = synthesis_file.read_text(encoding="utf-8")
    if not content.startswith("---"):
        raise ValueError("missing YAML front matter")
    metadata = yaml.safe_load(content.split("---", 2)[1])
    if not isinstance(metadata, dict):
        raise ValueError("front matter must be a YAML mapping")
    return metadata


def collect_synthesis_sources(entries: list[dict]) -> list[tuple[str, str, date, list[str]]]:
    """Deduplicate registry rows that intentionally point to the same synthesis."""
    grouped: dict[str, dict] = {}
    for entry in entries:
        synthesis = entry["synthesis_path"]
        group = grouped.setdefault(synthesis, {"primaries": [], "ids": []})
        group["primaries"].append(entry["dossier_path"])
        group["ids"].append(entry["dossier_id"])

    records = []
    for synthesis, group in grouped.items():
        synthesis_file = ROOT / synthesis
        if not synthesis_file.is_file():
            raise ValueError(f"missing synthesis: {synthesis}")
        metadata = read_metadata(synthesis_file)
        reviewed = date.fromisoformat(str(metadata["last_reviewed"]))
        related = metadata.get("related_dossiers", [])
        if not isinstance(related, list) or not related:
            raise ValueError(f"{synthesis}: related_dossiers must be a non-empty list")
        if len(related) != len(set(related)):
            raise ValueError(f"{synthesis}: duplicate related_dossiers")
        missing_primaries = sorted(set(group["primaries"]) - set(related))
        if missing_primaries:
            raise ValueError(f"{synthesis}: primary dossiers absent from related_dossiers: {missing_primaries}")
        for dossier in related:
            if not isinstance(dossier, str) or not (ROOT / dossier).is_file():
                raise ValueError(f"{synthesis}: missing related dossier {dossier!r}")
        records.append((synthesis, ", ".join(sorted(set(group["ids"]))), reviewed, related))
    return records


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or {}
    rows = []
    stale = unknown = 0
    try:
        records = collect_synthesis_sources(data.get("dossiers", []))
        for synthesis, dossier_ids, reviewed, related in records:
            for dossier in related:
                source_date = latest_commit_date(dossier)
                status = classify_source(reviewed, source_date)
                stale += status == "À RÉVISER"
                unknown += status == "INCONNU"
                detail = f"dernier commit : {source_date or 'inconnu'} ; revue déclarée : {reviewed}"
                rows.append((dossier_ids, dossier, synthesis, status, detail))
    except (KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: invalid synthesis freshness metadata: {exc}", file=sys.stderr)
        return 2

    report = [
        "### Fraîcheur des synthèses", "",
        "> Contrôle indicatif de tous les dossiers déclarés dans related_dossiers, comparés à last_reviewed. "
        "Une alerte invite à examiner les changements ; elle ne prouve pas que la synthèse est obsolète.", "",
        "| Dossier(s) principal(aux) | Document source | Synthèse | État | Détail |",
        "|---|---|---|---|---|",
    ]
    report.extend(
        f"| {ids} | {dossier} | {synthesis} | **{status}** | {detail} |"
        for ids, dossier, synthesis, status, detail in rows
    )
    report.extend([
        "",
        f"**Bilan des documents sources :** {stale} à réviser ; {unknown} sans historique exploitable ; "
        f"{len(rows) - stale - unknown} sans modification postérieure détectée.",
        "",
        "L'absence d'alerte ne garantit ni l'actualité des sources externes ni la validité des conclusions.",
    ])
    rendered = "\n".join(report)
    print(rendered)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(rendered + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
