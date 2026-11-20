#!/usr/bin/env python3
"""List exact metadata matches before ingesting sources into Society Lab."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from string import ascii_lowercase, ascii_uppercase
import sys
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "validate"))

from validate_registry import load_batch_validator, validate_batch_manifest  # noqa: E402


DOI_PATTERN = re.compile(r"10\.[0-9]{4,}/\S+")
DOI_RESOLVERS = {"doi.org", "dx.doi.org"}
ASCII_LOWERCASE = str.maketrans(ascii_uppercase, ascii_lowercase)


def resolver_doi(url: str) -> str:
    try:
        parsed = urlsplit(url)
        if parsed.scheme in {"http", "https"} and parsed.netloc.lower() in DOI_RESOLVERS:
            return unquote(parsed.path[1:])
    except ValueError:
        return ""
    return ""


def normalize_doi(identifier: str, url: str) -> str:
    value = identifier.strip().translate(ASCII_LOWERCASE).removeprefix("doi:").strip()
    value = resolver_doi(value) or value
    if not DOI_PATTERN.fullmatch(value):
        value = resolver_doi(url)
    return value.translate(ASCII_LOWERCASE) if DOI_PATTERN.fullmatch(value) else ""


def build_report(sources: list[dict], batch: dict | None = None) -> dict:
    groups = defaultdict(lambda: {"source_ids": set(), "candidate_ids": set()})
    candidates = batch["candidates"] if batch is not None else []
    for records, member, id_field, url_field, doi_field, source_field in (
        (sources, "source_ids", "id", "url", "doi", "id"),
        (candidates, "candidate_ids", "candidate_id", "canonical_url", "external_identifier", "source_id"),
    ):
        for record in records:
            url = record.get(url_field, "").strip()
            keys = {
                "source_id": record.get(source_field, ""),
                "url": url,
                "doi": normalize_doi(record.get(doi_field, ""), url),
                "artifact_sha256": record.get("artifact_sha256", "").lower(),
            }
            for kind, value in keys.items():
                if value:
                    groups[kind, value][member].add(record[id_field])

    report = {"sources_checked": len(sources), "registry_collisions": []}
    if batch is not None:
        report.update(
            batch_id=batch["batch_id"],
            candidates_checked=len(candidates),
            decision_counts=dict(Counter(candidate["decision"] for candidate in candidates)),
            batch_matches=[],
        )
    for (kind, value), members in sorted(groups.items()):
        source_ids = sorted(members["source_ids"])
        candidate_ids = sorted(members["candidate_ids"])
        match = {"kind": kind, "value": value, "source_ids": source_ids}
        if len(source_ids) > 1:
            report["registry_collisions"].append(match)
        if candidate_ids and len(source_ids) + len(candidate_ids) > 1:
            report["batch_matches"].append({**match, "candidate_ids": candidate_ids})
    return report


def load_batch(path: Path, artifacts: list[list[str]], source_ids: set[str]) -> dict:
    batch = yaml.safe_load(path.read_text(encoding="utf-8"))
    error = next(load_batch_validator().iter_errors(batch), None)
    if error is not None:
        location = ".".join(map(str, error.absolute_path)) or "manifest"
        raise ValueError(f"invalid batch field {location} ({error.validator})")

    errors = []
    validate_batch_manifest(batch, str(path), source_ids, errors)
    if errors:
        raise ValueError("\n".join(errors))

    candidates = {record["candidate_id"]: record for record in batch["candidates"]}
    seen = set()
    for candidate_id, filename in artifacts:
        if candidate_id not in candidates or candidate_id in seen:
            raise ValueError(f"unknown or repeated candidate for --artifact: {candidate_id}")
        seen.add(candidate_id)
        artifact = Path(filename)
        if not artifact.is_file():
            raise ValueError(f"--artifact for {candidate_id} must point to a regular file")
        with artifact.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        declared = candidates[candidate_id].get("artifact_sha256")
        if declared is not None and declared.lower() != digest:
            raise ValueError(f"computed SHA-256 differs from the manifest for {candidate_id}")
        candidates[candidate_id]["artifact_sha256"] = digest
    return batch


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", type=Path, help="Ingestion batch manifest to compare with the canonical registry")
    parser.add_argument("--artifact", action="append", nargs=2, default=[], metavar=("CANDIDATE_ID", "PATH"),
                        help="Compute SHA-256 for a local file, repeatable for different candidates")
    args = parser.parse_args()
    if args.artifact and args.batch is None:
        parser.error("--artifact requires --batch")

    try:
        registry = ROOT / "sources" / "registry.yml"
        sources = yaml.safe_load(registry.read_text(encoding="utf-8"))["sources"]
        source_ids = {source["id"] for source in sources}
        batch = load_batch(args.batch, args.artifact, source_ids) if args.batch is not None else None
        report = build_report(sources, batch)
    except (OSError, KeyError, TypeError, ValueError, SchemaError) as exc:
        parser.error(str(exc))
    except yaml.YAMLError:
        parser.error("invalid YAML in the registry or batch manifest")
    print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main()
