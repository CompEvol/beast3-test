#!/usr/bin/env python3
"""Take a snapshot of a beast3 milestone for the status site: reports/milestone.json.

Lists the open issues on the milestone and every open pull request of the repository, with
the state of its checks and reviews. The site is built from the committed snapshot, so run
this and commit the result when the page should be brought up to date.

Needs the GitHub command line tool `gh`, logged in. Standard library only.

Usage: scripts/fetch_milestone.py [--milestone 2.8.0] [--repo CompEvol/beast3]
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def gh(*args):
    try:
        out = subprocess.run(["gh"] + list(args), capture_output=True, text=True, check=True).stdout
    except FileNotFoundError:
        sys.exit("gh not found: install the GitHub command line tool")
    except subprocess.CalledProcessError as e:
        sys.exit("gh %s failed:\n%s" % (" ".join(args), e.stderr))
    return json.loads(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--milestone", default="2.8.0")
    ap.add_argument("--repo", default="CompEvol/beast3")
    ap.add_argument("--out", default=os.path.join(ROOT, "reports", "milestone.json"))
    a = ap.parse_args()

    issues = gh("issue", "list", "-R", a.repo, "--milestone", a.milestone, "--state", "open", "--limit", "500",
                "--json", "number,title,url,author,createdAt,updatedAt,labels,assignees,comments")
    prs = gh("pr", "list", "-R", a.repo, "--state", "open", "--limit", "200", "--json",
             "number,title,url,author,milestone,isDraft,reviewDecision,reviews,statusCheckRollup,"
             "closingIssuesReferences,updatedAt")
    closed = gh("issue", "list", "-R", a.repo, "--milestone", a.milestone, "--state", "closed", "--limit", "500",
                "--json", "number")

    def checks(pr):
        results = set((c.get("conclusion") or c.get("state") or "PENDING") for c in pr.get("statusCheckRollup") or [])
        if not results:
            return "none"
        if results <= {"SUCCESS", "SKIPPED", "NEUTRAL"}:
            return "pass"
        if results & {"FAILURE", "ERROR", "TIMED_OUT", "CANCELLED"}:
            return "fail"
        return "running"

    def review(pr):
        decision = pr.get("reviewDecision") or ""
        if decision == "APPROVED":
            return "approved"
        if decision == "CHANGES_REQUESTED":
            return "changes requested"
        return "commented" if pr.get("reviews") else "none yet"

    snapshot = {
        "repo": a.repo,
        "milestone": a.milestone,
        "fetched": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "closed": len(closed),
        "issues": [{
            "number": i["number"], "title": i["title"], "url": i["url"], "author": i["author"]["login"],
            "created": i["createdAt"][:10], "updated": i["updatedAt"][:10],
            "labels": [l["name"] for l in i["labels"]], "assignees": [x["login"] for x in i["assignees"]],
            "comments": len(i["comments"]),
        } for i in sorted(issues, key=lambda i: -i["number"])],
        "prs": [{
            "number": p["number"], "title": p["title"], "url": p["url"], "author": p["author"]["login"],
            "milestone": (p.get("milestone") or {}).get("title", ""), "draft": p["isDraft"],
            "closes": [c["number"] for c in p.get("closingIssuesReferences") or []],
            "checks": checks(p), "review": review(p), "updated": p["updatedAt"][:10],
        } for p in sorted(prs, key=lambda p: -p["number"])],
    }
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(snapshot, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("%s: %d open issue(s) on %s, %d closed, %d open pull request(s)" % (
        os.path.relpath(a.out, ROOT), len(snapshot["issues"]), a.milestone, snapshot["closed"], len(snapshot["prs"])))


if __name__ == "__main__":
    main()
