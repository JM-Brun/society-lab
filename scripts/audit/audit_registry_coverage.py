#!/usr/bin/env python3
"""Audit file -> canonical registry -> JSON Schema -> validator coverage.

This is an inventory only: it does not rewrite records, infer missing facts, or
change schema requiredness. Run from any directory with PyYAML installed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[2]
TARGETS = (
    ("Source", "sources/registry.yml", "sources", "schemas/source.schema.json", "SOURCE", "sources"),
    ("Study", "research/studies/registry.yml", "studies", "schemas/study.schema.json", "STUDY", "research/studies"),
    ("Dataset", "research/datasets/registry.yml", "datasets", "schemas/dataset.schema.json", "DATASET", "research/datasets"),
    ("Claim", "claims/registry.yml", "claims", "schemas/claim.schema.json", "CLAIM", "claims"),
    ("Hypothesis", "hypotheses/registry.yml", "hypotheses", "schemas/hypothesis.schema.json", "HYPOTHESIS", "hypotheses"),
    ("Forecast", "forecasts/registry.yml", "forecasts", "schemas/forecast.schema.json", "FORECAST", "forecasts"),
    ("Dossier", "dossiers/registry.yml", "dossiers", "schemas/dossier.schema.json", "DOSSIER", "dossiers"),
    ("Concept", "knowledge/concepts/registry.yml", "concepts", "schemas/concept.schema.json", "CONCEPT", "knowledge/concepts"),
    ("Mechanism", "knowledge/mechanisms/registry.yml", "mechanisms", "schemas/mechanism.schema.json", "MECHANISM", "knowledge/mechanisms"),
)
VALIDATOR = "scripts/validate/validate_registry.py"


def read_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = yaml.safe_load(stream) or {}
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a YAML mapping")
    return value


def inventory(target: tuple[str, str, str, str, str, str]) -> dict[str, Any]:
    label, registry_rel, collection, schema_rel, prefix, directory = target
    registry_path, schema_path = ROOT / registry_rel, ROOT / schema_rel
    payload = read_yaml(registry_path)
    records = payload.get(collection, [])
    if not isinstance(records, list) or not all(isinstance(row, dict) for row in records):
        raise ValueError(f"{registry_rel}: {collection} must be a list of mappings")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    properties = schema.get("properties", {})
    required = set(schema.get("required", []))
    counts = {name: sum(name in row and row[name] is not None for row in records) for name in properties}
    observed = sorted({name for row in records for name in row})
    unknown = sorted(set(observed) - set(properties))
    files = sorted((ROOT / directory).glob("*.yml")) + sorted((ROOT / directory).glob("*.yaml"))
    return {
        "label": label,
        "registry": registry_rel,
        "collection": collection,
        "schema": schema_rel,
        "prefix": prefix,
        "records": len(records),
        "record_files": len(files),
        "required": sorted(required),
        "properties": properties,
        "counts": counts,
        "observed": observed,
        "unknown": unknown,
        "missing_required": sorted(name for name in required if counts.get(name, 0) != len(records)),
    }


def render(items: list[dict[str, Any]]) -> str:
    lines = [
        "# Inventaire automatisé — fichiers, registres, schémas et validateurs",
        "",
        "Généré par `scripts/audit/audit_registry_coverage.py`. Cet inventaire décrit la couverture actuelle ;",
        "il ne définit pas les exigences métier par étape et ne déclenche aucune migration.",
        "",
        "## Chaîne de contrôle",
        "",
        "| Objet | Fichiers YAML dans le répertoire | Registre canonique / collection | Schéma JSON | Validateur | Fiches |",
        "|---|---:|---|---|---|---:|",
    ]
    for item in items:
        lines.append(
            f"| {item['label']} | {item['record_files']} | `{item['registry']}#{item['collection']}` "
            f"| `{item['schema']}` | `{VALIDATOR}` | {item['records']} |"
        )
    lines += ["", "## Couverture des propriétés", ""]
    for item in items:
        lines += [
            f"### {item['label']} — {item['records']} fiches",
            "",
            f"Registre : `{item['registry']}` · Schéma : `{item['schema']}`",
            "",
            "| Propriété | Présence | Requise par le schéma |",
            "|---|---:|:---:|",
        ]
        for name in sorted(item["properties"]):
            marker = "oui" if name in item["required"] else "non"
            lines.append(f"| `{name}` | {item['counts'].get(name, 0)}/{item['records']} | {marker} |")
        lines += ["", f"Propriétés observées hors schéma : {', '.join(item['unknown']) if item['unknown'] else 'aucune'}.", ""]
        if item["missing_required"]:
            lines.append("**Anomalie à investiguer :** propriétés déclarées obligatoires mais absentes d'au moins une fiche : "
                         + ", ".join(f"`{name}`" for name in item["missing_required"]) + ".")
        else:
            lines.append("Toutes les propriétés obligatoires sont présentes dans chaque fiche (contrôle de présence uniquement).")
        lines.append("")
    lines += [
        "## Limites et interprétation",
        "",
        "- Le nombre de fichiers YAML inclut le registre lui-même ; il ne signifie pas que chaque fiche est stockée dans un fichier distinct.",
        "- La présence d'une propriété ne vérifie ni sa qualité, ni sa précision, ni la validité de ses références.",
        "- Les champs imbriqués (par exemple `scope`, `source_verifications` ou `provenance`) sont comptés comme propriétés de premier niveau ; leur couverture interne doit faire l'objet d'un audit dédié.",
        "- Les contraintes conditionnelles et les exigences par étape du pipeline ne sont pas déduites de `required`.",
        "- Le validateur principal est référencé comme point d'entrée ; les contrôles transversaux et leurs conditions d'exécution restent à cartographier séparément.",
        "",
        "## Décision",
        "",
        "Ne pas rendre globalement obligatoires les propriétés facultatives sur la seule base de cet inventaire. Construire ensuite une matrice par étape : découverte, qualification de source, extraction, analyse, vérification d'un claim et publication.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write Markdown report to this path instead of stdout")
    args = parser.parse_args()
    items = [inventory(target) for target in TARGETS]
    report = render(items)
    if args.output:
        destination = args.output if args.output.is_absolute() else ROOT / args.output
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
