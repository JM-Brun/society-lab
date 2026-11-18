#!/usr/bin/env python3
"""Generate a multidimensional Markdown view from GitHub and canonical registries."""
from __future__ import annotations
import json, os, sys, urllib.error, urllib.request
from pathlib import Path
from datetime import datetime, timezone
import yaml
API = "https://api.github.com"

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

def render_markdown(rows, generated_at):
    priorities=["priority:high","priority:medium","priority:low","unclassified"]
    lines=["# Backlog Society Lab","",f"> Généré le {generated_at} depuis les issues GitHub ouvertes et les registres canoniques. Vue indicative, non décisionnelle.","",
      f"- Issues ouvertes : **{len(rows)}**",f"- Correspondance explicite : **{sum(row['mapping_valid'] for row in rows)}**",
      f"- À qualifier : **{sum(not row['mapping_valid'] for row in rows)}**",
      f"- Priorité invalide ou absente : **{sum(not row['priority_valid'] for row in rows)}**","",
      "Les domaines proviennent exclusivement des dossiers référencés. Les dépendances proviennent exclusivement du mapping explicite. Aucune inférence depuis les titres ou mots-clés.",""]
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

def main():
    repository=os.environ.get("GITHUB_REPOSITORY","JM-Brun/society-lab"); token=os.environ.get("GITHUB_TOKEN")
    if not token: print("GITHUB_TOKEN est requis.",file=sys.stderr); return 2
    root=Path(__file__).resolve().parents[2]
    mapping=load_yaml(root/"governance/issue-domain-map.yml"); dossiers=load_yaml(root/"dossiers/registry.yml")
    rows=build_rows(fetch_open_issues(repository,token),mapping,dossiers)
    output=render_markdown(rows,datetime.now(timezone.utc).isoformat(timespec="minutes"))
    target=Path(os.environ.get("BACKLOG_OUTPUT","backlog-view.md")); target.write_text(output,encoding="utf-8")
    summary=os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary,"a",encoding="utf-8") as stream: stream.write(output)
    print(f"Generated {target} for {len(rows)} open issues."); return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except (urllib.error.URLError,KeyError,ValueError,OSError) as exc:
        print(f"Backlog generation failed: {exc}",file=sys.stderr); raise SystemExit(2)