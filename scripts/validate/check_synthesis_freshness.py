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


def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    rows = []
    stale = unknown = 0

    for entry in data.get("dossiers", []):
        synthesis = entry["synthesis_path"]
        synthesis_file = ROOT / synthesis
        if not synthesis_file.is_file():
            print(f"ERROR: missing synthesis: {synthesis}", file=sys.stderr)
            return 2
        try:
            metadata = read_metadata(synthesis_file)
            reviewed = date.fromisoformat(str(metadata["last_reviewed"]))
            related = metadata.get("related_dossiers", [])
            if not isinstance(related, list) or not related:
                raise ValueError("related_dossiers must be a non-empty list")
        except (KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
            print(f"ERROR: invalid metadata in {synthesis}: {exc}", file=sys.stderr)
            return 2

        primary = entry["dossier_path"]
        if primary not in related:
            print(f"ERROR: {synthesis} does not list primary dossier {primary}", file=sys.stderr)
            return 2

        for dossier in related:
            if not isinstance(dossier, str) or not (ROOT / dossier).is_file():
                print(f"ERROR: missing related dossier {dossier!r} in {synthesis}", file=sys.stderr)
                return 2
            source_date = latest_commit_date(dossier)
            status = classify_source(reviewed, source_date)
            if status == "À RÉVISER":
                stale += 1
            elif status == "INCONNU":
                unknown += 1
            detail = (
                f"dernier commit : {source_date or 'inconnu'} ; "
                f"revue déclarée : {reviewed}"
            )
            rows.append((entry["dossier_id"], dossier, synthesis, status, detail))

    report = [
        "### Fraîcheur des synthèses", "",
        "> Contrôle indicatif de tous les dossiers déclarés dans related_dossiers, comparés à last_reviewed. "
        "Une alerte invite à examiner les changements ; elle ne prouve pas que la synthèse est obsolète.", "",
        "| Dossier principal | Document source | Synthèse | État | Détail |",
        "|---|---|---|---|---|",
    ]
    report.extend(
        f"| {identifier} | {dossier} | {synthesis} | **{status}** | {detail} |"
        for identifier, dossier, synthesis, status, detail in rows
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
