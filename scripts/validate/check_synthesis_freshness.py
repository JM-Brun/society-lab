#!/usr/bin/env python3
"""Advisory freshness report for subject syntheses."""
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

def main() -> int:
    data = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    rows = []
    stale = unknown = 0
    for entry in data.get("dossiers", []):
        dossier, synthesis = entry["dossier_path"], entry["synthesis_path"]
        synthesis_file = ROOT / synthesis
        if not synthesis_file.is_file():
            print(f"ERROR: missing synthesis: {synthesis}", file=sys.stderr)
            return 2
        content = synthesis_file.read_text(encoding="utf-8")
        if not content.startswith("---"):
            print(f"ERROR: missing YAML front matter: {synthesis}", file=sys.stderr)
            return 2
        try:
            metadata = yaml.safe_load(content.split("---", 2)[1])
            reviewed = date.fromisoformat(str(metadata["last_reviewed"]))
        except (IndexError, KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
            print(f"ERROR: invalid last_reviewed in {synthesis}: {exc}", file=sys.stderr)
            return 2
        source_date = latest_commit_date(dossier)
        if source_date is None:
            status, detail = "INCONNU", "aucun historique Git disponible"
            unknown += 1
        elif source_date > reviewed:
            status, detail = "À RÉVISER", f"dossier modifié le {source_date}, revue déclarée le {reviewed}"
            stale += 1
        else:
            status, detail = "AUCUNE ALERTE", f"dossier modifié le {source_date}, revue déclarée le {reviewed}"
        rows.append((entry["dossier_id"], synthesis, status, detail))
    report = [
        "### Fraîcheur des synthèses", "",
        "> Contrôle indicatif fondé sur le dernier commit du dossier et la date éditoriale last_reviewed. "
        "Un avertissement signale une revue potentiellement nécessaire ; il ne prouve pas que la conclusion est obsolète.", "",
        "| Dossier | Synthèse | État | Détail |", "|---|---|---|---|",
    ]
    report.extend(f"| {d} | {s} | **{state}** | {detail} |" for d, s, state, detail in rows)
    report.extend(["", f"**Bilan :** {stale} à réviser ; {unknown} sans historique exploitable ; "
                   f"{len(rows) - stale - unknown} sans modification postérieure détectée.", "",
                   "L'absence d'alerte ne garantit ni l'actualité des sources externes ni la validité des conclusions."])
    rendered = "\n".join(report)
    print(rendered)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write(rendered + "\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
