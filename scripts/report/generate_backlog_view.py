#!/usr/bin/env python3
"""Generate a Markdown backlog view from GitHub or replay a captured snapshot."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

API = "https://api.github.com"
ROOT = Path(__file__).resolve().parents[2]
MAPPING = "governance/issue-domain-map.yml"
DOSSIERS = "dossiers/registry.yml"
SNAPSHOT_VERSION = 1

def load_yaml(path):
    with path.open(encoding="utf-8") as stream: return yaml.safe_load(stream)

def fetch_open_issues(repository, token):
    url = f"{API}/repos/{repository}/issues?state=open&per_page=100"
    headers = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","Authorization":f"Bearer {token}","User-Agent":"society-lab-backlog-view"}
    result = []
    while url:
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=30) as response:
            result.extend(item for item in json.load(response) if "pull_request" not in item)
            link = response.headers.get("Link", "")
        url = next((part[part.find("<")+1:part.find(">")] for part in link.split(",") if 'rel="next"' in part), None)
    return result

def build_rows(issues, mapping, dossier_registry):
    mapping_by_number = {item["issue"]: item for item in mapping.get("issues", [])}
    dossiers = {item["id"]: item for item in dossier_registry.get("dossiers", [])}
    rows = []
    for issue in issues:
        number = issue["number"]; mapped = mapping_by_number.get(number)
        labels = sorted(label["name"] for label in issue.get("labels", []))
        priorities = [label for label in labels if label.startswith("priority:")]
        dossier_ids = mapped.get("dossier_ids", []) if mapped else []
        domain_ids = sorted({domain for dossier_id in dossier_ids for domain in dossiers.get(dossier_id, {}).get("domain_ids", [])})
        rows.append({"number":number,"title":issue["title"],"url":issue["html_url"],"labels":labels,
          "priority":priorities[0] if len(priorities)==1 and priorities[0] in {"priority:high","priority:medium","priority:low"} else "unclassified","priority_valid":len(priorities)==1 and priorities[0] in {"priority:high","priority:medium","priority:low"},
          "nature":[label for label in labels if label in {"research","data","documentation","enhancement","knowledge-graph"}],
          "kind":mapped.get("kind","unmapped") if mapped else "unmapped","dossier_ids":dossier_ids,
          "domain_ids":domain_ids,"depends_on":mapped.get("depends_on",[]) if mapped else [],
          "mapping_valid":mapped is not None and all(item in dossiers for item in dossier_ids)})
    return sorted(rows,key=lambda row:(row["priority"],row["number"]))

def render_markdown(rows, captured_at, *, source_revision=None):
    priorities=["priority:high","priority:medium","priority:low","unclassified"]
    lines = ["# Backlog Society Lab", "", f"> Issues GitHub ouvertes relevées le {captured_at}."]
    if source_revision is not None:
        lines.append(f"> Révision Git de la correspondance et des dossiers `{source_revision}`.")
    lines.extend(["",
      f"- Issues ouvertes : **{len(rows)}**",f"- Correspondance explicite : **{sum(row['mapping_valid'] for row in rows)}**",
      f"- À qualifier : **{sum(not row['mapping_valid'] for row in rows)}**",
      f"- Priorité invalide ou absente : **{sum(not row['priority_valid'] for row in rows)}**","",
      "Les domaines proviennent des dossiers référencés. Les dépendances viennent de la correspondance explicite.", ""])
    for priority in priorities:
        selected=[row for row in rows if row["priority"]==priority]
        lines.extend([f"## {priority} ({len(selected)})",""])
        for row in selected:
            domains=", ".join(row["domain_ids"]) or "transversal / non associé"
            nature=", ".join(row["nature"]) or "nature non renseignée"
            dossiers=", ".join(row["dossier_ids"]) or "aucun dossier associé"
            dependencies=", ".join(f"#{n}" for n in row["depends_on"]) or "aucune dépendance déclarée"
            warning=" ⚠️ mapping ou priorité à vérifier" if not row["mapping_valid"] or not row["priority_valid"] else ""
            lines.append(f"- [#{row['number']} — {row['title']}]({row['url']}) — {row['kind']} ; {nature} ; domaines : {domains} ; dossiers : {dossiers} ; dépendances : {dependencies}{warning}")
        lines.append("")
    lines.extend(["## À qualifier",""])
    unmapped=[row for row in rows if not row["mapping_valid"]]
    lines.extend([f"- [#{row['number']} — {row['title']}]({row['url']})" for row in unmapped] or ["Aucune issue non mappée."])
    lines.append(""); return "\n".join(lines)

def read_git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, encoding="utf-8",
    ).stdout


def capture_snapshot(repository, token):
    revision = read_git("rev-parse", "--verify", "HEAD").strip()
    mapping = yaml.safe_load(read_git("show", f"{revision}:{MAPPING}"))
    dossiers = yaml.safe_load(read_git("show", f"{revision}:{DOSSIERS}"))
    issues = fetch_open_issues(repository, token)
    issue_numbers = {issue["number"] for issue in issues}
    mapped = [
        {key: value for key, value in row.items() if key in {"issue", "dossier_ids", "depends_on", "kind"}}
        for row in mapping.get("issues", []) if row["issue"] in issue_numbers
    ]
    dossier_ids = {identifier for row in mapped for identifier in row.get("dossier_ids", [])}
    return {
        "version": SNAPSHOT_VERSION,
        "repository": repository,
        "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_revision": revision,
        "issues": [
            {"number": issue["number"], "title": issue["title"], "html_url": issue["html_url"],
             "labels": [{"name": name} for name in sorted(label["name"] for label in issue.get("labels", []))]}
            for issue in sorted(issues, key=lambda item: item["number"])
        ],
        "mapping": {"issues": mapped},
        "dossiers": {"dossiers": [
            {"id": row["id"], "domain_ids": row.get("domain_ids", [])}
            for row in dossiers.get("dossiers", []) if row["id"] in dossier_ids
        ]},
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    snapshot_options = parser.add_mutually_exclusive_group()
    snapshot_options.add_argument("--snapshot-output", type=Path, help="Save inputs from GitHub and the current Git commit")
    snapshot_options.add_argument("--snapshot-input", type=Path, help="Replay this snapshot without API or Git access")
    args = parser.parse_args(argv)
    target = Path(os.environ.get("BACKLOG_OUTPUT", "backlog-view.md"))
    snapshot_path = args.snapshot_input or args.snapshot_output
    if snapshot_path is not None and snapshot_path.resolve() == target.resolve():
        parser.error("The snapshot and Markdown output require different paths")

    if args.snapshot_input is not None:
        snapshot = json.loads(args.snapshot_input.read_text(encoding="utf-8"))
        if not isinstance(snapshot, dict) or snapshot.get("version") != SNAPSHOT_VERSION:
            raise ValueError(f"Expected a backlog snapshot with version {SNAPSHOT_VERSION}")
    else:
        repository = os.environ.get("GITHUB_REPOSITORY", "JM-Brun/society-lab")
        token = os.environ.get("GITHUB_TOKEN")
        if not token:
            parser.error("GITHUB_TOKEN est requis pour consulter GitHub")
        if args.snapshot_output is not None:
            snapshot = capture_snapshot(repository, token)
        else:
            issues = fetch_open_issues(repository, token)
            snapshot = {
                "issues": issues,
                "mapping": load_yaml(ROOT / MAPPING),
                "dossiers": load_yaml(ROOT / DOSSIERS),
                "captured_at": datetime.now(timezone.utc).isoformat(timespec="minutes"),
            }

    rows = build_rows(snapshot["issues"], snapshot["mapping"], snapshot["dossiers"])
    output = render_markdown(rows, snapshot["captured_at"], source_revision=snapshot.get("source_revision"))
    target.write_text(output, encoding="utf-8")
    if args.snapshot_output is not None:
        serialized = json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True)
        args.snapshot_output.write_text(serialized + "\n", encoding="utf-8")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write(output)
    print(f"Generated {target} for {len(rows)} open issues.")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Backlog generation failed: {exc.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2)
    except (KeyError, ValueError, TypeError, OSError, yaml.YAMLError) as exc:
        print(f"Backlog generation failed: {exc}", file=sys.stderr)
        raise SystemExit(2)
