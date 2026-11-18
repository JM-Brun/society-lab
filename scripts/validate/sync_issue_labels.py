#!/usr/bin/env python3
"""Compare/synchronize canonical GitHub labels. Read-only unless --apply is explicit."""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

API = "https://api.github.com"
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "JM-Brun/society-lab")
TOKEN = os.environ.get("GITHUB_TOKEN")


@dataclass(frozen=True)
class Drift:
    name: str
    kind: str
    detail: str


def canonical_labels(policy: dict) -> dict[str, dict[str, str]]:
    result = {}
    for axis in policy["axes"].values():
        for name, metadata in axis.items():
            if name in result:
                raise ValueError(f"Label déclaré plusieurs fois : {name}")
            result[name] = {
                "name": name,
                "color": metadata["color"].removeprefix("#").lower(),
                "description": metadata.get("description", ""),
            }
    return result


def compare_labels(expected: dict, actual: dict) -> list[Drift]:
    drift = []
    for name, wanted in sorted(expected.items()):
        found = actual.get(name)
        if found is None:
            drift.append(Drift(name, "missing", "label absent sur GitHub"))
            continue
        fields = []
        for field in ("color", "description"):
            current = (found.get(field) or "").lower() if field == "color" else (found.get(field) or "")
            target = wanted[field].lower() if field == "color" else wanted[field]
            if current != target:
                fields.append(f"{field}: GitHub={current!r}, canonique={target!r}")
        if fields:
            drift.append(Drift(name, "different", "; ".join(fields)))
    for name in sorted(set(actual) - set(expected)):
        drift.append(Drift(name, "unmanaged", "label GitHub non déclaré dans le référentiel (conservé)"))
    return drift


def request(url: str, method: str = "GET", payload: dict | None = None):
    if not TOKEN:
        raise RuntimeError("GITHUB_TOKEN est requis.")
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "society-lab-canonical-label-sync",
        "Authorization": f"Bearer {TOKEN}",
    }
    data = json.dumps(payload).encode() if payload is not None else None
    if data is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response), response.headers.get("Link", "")


def fetch_labels() -> dict:
    url = f"{API}/repos/{REPOSITORY}/labels?per_page=100"
    labels = {}
    while url:
        payload, link = request(url)
        for label in payload:
            labels[label["name"]] = label
        url = next((part[part.find("<") + 1:part.find(">")] for part in link.split(",") if 'rel="next"' in part), None)
    return labels


def synchronize(expected: dict, actual: dict, apply: bool) -> list[str]:
    actions = []
    for name, wanted in sorted(expected.items()):
        found = actual.get(name)
        if found is None:
            actions.append(f"CREATE {name}")
            if apply:
                request(f"{API}/repos/{REPOSITORY}/labels", "POST", wanted)
        else:
            patch = {key: wanted[key] for key in ("color", "description")
                     if ((found.get(key) or "").lower() != wanted[key].lower() if key == "color"
                         else (found.get(key) or "") != wanted[key])}
            if patch:
                actions.append(f"UPDATE {name}: {', '.join(sorted(patch))}")
                if apply:
                    request(f"{API}/repos/{REPOSITORY}/labels/{urllib.parse.quote(name, safe='')}", "PATCH", patch)
    return actions


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="create/update canonical labels (never deletes)")
    args = parser.parse_args()
    if args.apply and os.environ.get("ALLOW_LABEL_SYNC") != "true":
        parser.error("--apply exige ALLOW_LABEL_SYNC=true (confirmation explicite du workflow)")
    with open("governance/issue-labels.json", encoding="utf-8") as handle:
        expected = canonical_labels(json.load(handle))
    actual = fetch_labels()
    drift = compare_labels(expected, actual)
    actions = synchronize(expected, actual, args.apply)
    counts = {kind: sum(item.kind == kind for item in drift) for kind in ("missing", "different", "unmanaged")}
    mode = "APPLICATION EXPLICITE" if args.apply else "DRY-RUN (lecture seule)"
    print(f"## Synchronisation des labels — {REPOSITORY}")
    print(f"Mode : **{mode}**")
    print(f"Labels canoniques : {len(expected)} ; labels GitHub observés : {len(actual)}")
    print(f"Dérives : {counts['missing']} absents, {counts['different']} divergents, {counts['unmanaged']} non gérés")
    for item in drift:
        print(f"- [{item.kind}] {item.name} — {item.detail}")
    if actions:
        print("\nActions proposées/exécutées :")
        for action in actions:
            print(f"- {action}")
    else:
        print("\nAucune création ou mise à jour nécessaire.")
    print("\nAucun label non canonique ne sera supprimé ; aucune issue ne sera modifiée.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (urllib.error.URLError, KeyError, ValueError, RuntimeError) as exc:
        print(f"Échec de la synchronisation des labels : {exc}", file=sys.stderr)
        raise SystemExit(2)
