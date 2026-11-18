#!/usr/bin/env python3
"""Read-only audit of open GitHub issues against the issue-label policy."""
from __future__ import annotations
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "JM-Brun/society-lab")
TOKEN = os.environ.get("GITHUB_TOKEN")
PRIORITIES = {"priority:high", "priority:medium", "priority:low"}

def request(url: str):
    headers = {"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28","User-Agent":"society-lab-issue-governance-audit"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response), response.headers.get("Link", "")

def pages():
    url = f"{API}/repos/{REPOSITORY}/issues?state=open&per_page=100"
    while url:
        payload, link = request(url)
        for item in payload:
            if "pull_request" not in item:
                yield item
        url = next((part[part.find("<")+1:part.find(">")] for part in link.split(",") if 'rel="next"' in part), None)

def main() -> int:
    with open("governance/issue-labels.json", encoding="utf-8") as handle:
        policy = json.load(handle)
    declared = [name for axis in policy["axes"].values() for name in axis]
    if len(declared) != len(set(declared)) or not PRIORITIES.issubset(set(declared)):
        print("ERREUR: taxonomie incohérente ou priorités manquantes.", file=sys.stderr)
        return 2
    issues = list(pages())
    problems = []
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        missing = []
        if "internal" not in labels:
            missing.append("internal absent")
        count = len(labels & PRIORITIES)
        if count == 0:
            missing.append("priorité absente")
        elif count > 1:
            missing.append("plusieurs priorités")
        if missing:
            problems.append((issue["number"], issue["title"], ", ".join(missing)))
    lines = ["## Audit des labels — " + REPOSITORY, "", f"Issues ouvertes examinées : **{len(issues)}**", f"Issues conformes aux invariants mécaniques : **{len(issues)-len(problems)}**", f"Issues à revoir : **{len(problems)}**", ""]
    if problems:
        lines += ["| Issue | Anomalies |", "|---|---|"]
        for number, title, reason in problems:
            lines.append(f"| [#{number}](https://github.com/{REPOSITORY}/issues/{number}) — {title.replace('|', '/')} | {reason} |")
    else:
        lines.append("Aucune anomalie mécanique détectée.")
    lines += ["", "> Audit en lecture seule. Il ne décide pas si meta ou le niveau de priorité sont justifiés."]
    report = "\n".join(lines) + "\n"
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            handle.write(report)
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (urllib.error.URLError, KeyError, ValueError) as exc:
        print(f"Échec de l'audit des issues : {exc}", file=sys.stderr)
        raise SystemExit(2)
