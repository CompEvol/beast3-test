#!/usr/bin/env python3
"""Build the validation status site (GitHub Pages) from files in the repo.

Pages:
  index.html     goal of the testing, with a summary of and link to each track
  beauti.html    BEAUti by hand, C01-C30
  examples.html  the BEAST 2 example XMLs and their BEAST 3 conversions
  milestone.html open issues and pull requests of the beast3 release milestone

Inputs:
  reports/status.tsv, reports/status-notes.md                 BEAUti: hand-set status, note; panels
  reports/examples-status.tsv, reports/examples-notes.md      examples: tester, status, note; panels
  reports/summary/batch-summary.md   min ESS and max z per name (compare.py --all)
  ASSIGNMENTS.md                     BEAUti tester and model per combination
  README.md                          example inventory (converted, converted in)
  reports/milestone.json             milestone: snapshot of GitHub (scripts/fetch_milestone.py)
  reports/milestone-triage.tsv, reports/milestone-notes.md    milestone: hand-set group, note; panels
  scripts/status_page.html           page layout

Usage: scripts/build_status_page.py [--out _site]

Each track page lists entries whose status disagrees with the numbers; these are printed too.
Exits non-zero only if an input is missing or malformed.
"""
import argparse
import datetime
import html
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BEAUTI_STATUSES = {
    "pass": ["Passed", "Matched, no flags, full chains"],
    "explained": ["Passed, explained", "Flag due to a known difference"],
    "partial": ["Matched, runs short", "Most runs stopped early"],
    "rerun": ["Rerun needed", "rc1 build or a flag to recheck"],
    "blocked": ["Needs rc3", "Fix landed after rc2"],
    "fail": ["Not matched", "Unexplained difference"],
    "none": ["Not run yet", "No results in the repo"],
}
EXAMPLE_STATUSES = {
    "pass": ["Passed", "Matched, no flags"],
    "explained": ["Passed, explained", "Flag due to a known difference"],
    "open": ["Decision needed", "Conversion differs, or not converted"],
    "blocked": ["Needs rc3", "Fix landed after rc2"],
    "none": ["Not run yet", "No results in the repo"],
}
MILESTONE_GROUPS = {
    "review": ["Fix in review", "An open pull request fixes it"],
    "todo": ["To fix", "Clear what to do, nobody on it yet"],
    "decide": ["Decide", "2.8.0, later, or close"],
    "release": ["Release work", "Builds, checks and umbrella issues"],
    "close": ["Check and close", "Looks done already"],
    "new": ["Not sorted", "New since the list was sorted"],
}
PASSED = ("pass", "explained")
# pages that are not validation tracks: (file, label in the navigation)
EXTRA_PAGES = [("milestone.html", "2.8.0 milestone")]
ID_RE = re.compile(r"C\d{2}")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def esc(text):
    return html.escape(text, quote=False)


def inline(text):
    """Escape text and convert `code`, **bold** and [links](url)."""
    out = esc(text)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)
    out = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', out)
    return out


def plain(md):
    """Strip markdown links, bold and backticks from a table cell."""
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    return md.replace("**", "").replace("`", "").strip()


def md_rows(text):
    """Cells of every markdown table row."""
    for line in text.splitlines():
        if line.startswith("|") and not re.match(r"\|\s*-", line):
            yield [c.strip() for c in line.strip().strip("|").split("|")]


def tsv(path, ncols, valid, key_ok):
    rows = {}
    for n, line in enumerate(read(path).splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = [p.strip() for p in line.split("\t")]
        parts += [""] * (ncols - len(parts))
        key, status = parts[0], parts[ncols - 2]
        if not key_ok(key) or status not in valid:
            sys.exit("%s line %d: bad key or status (one of %s): %r" % (path, n, ", ".join(valid), line))
        if key in rows:
            sys.exit("%s line %d: %s listed twice" % (path, n, key))
        rows[key] = parts[1:ncols]
    return rows


def load_batch():
    """batch-summary.md: Name | Reps | Min ESS | Max z | Max clade | Flagged | Verdict."""
    def num(cell, kind):
        try:
            return kind(cell)
        except ValueError:
            return None
    out = {}
    for c in md_rows(read("reports/summary/batch-summary.md")):
        if len(c) >= 7 and c[0] != "Name":
            out[c[0]] = {"ess": num(c[2], int), "z": num(c[3], float), "verdict": c[6]}
    return out


def checks(status, batch, labels, keyname=lambda k: k):
    """Entries whose status disagrees with the numbers. status: key -> status code."""
    msgs = []
    for key, st in sorted(status.items()):
        b = batch.get(keyname(key))
        lab = labels[st][0].lower()
        if st == "none":
            if b:
                msgs.append("%s is marked not run, but batch-summary.md has results (%s)." % (key, b["verdict"]))
            continue
        if st == "open":
            continue
        if not b:
            msgs.append("%s is marked %s, but batch-summary.md has no row for it." % (key, lab))
            continue
        if st in ("pass", "partial"):
            if not b["verdict"].startswith("matched"):
                msgs.append("%s is marked %s, but the latest verdict is '%s'." % (key, lab, b["verdict"]))
            if b["z"] is not None and b["z"] >= 3:
                msgs.append("%s is marked %s, but max z is %g." % (key, lab, b["z"]))
        if st == "pass" and b["ess"] is not None and b["ess"] < 200:
            msgs.append("%s is marked passed, but min ESS is %d." % (key, b["ess"]))
    return msgs


def panels(path):
    text = re.sub(r"<!--.*?-->", "", read(path), flags=re.S)
    out, cur, items, kind = [], None, [], None

    def flush_list():
        nonlocal items, kind
        if items:
            cur.append("<%s>" % kind + "".join("<li>%s</li>" % i for i in items) + "</%s>" % kind)
        items, kind = [], None

    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            if cur is not None:
                flush_list()
                out.append(cur)
            cur = ["<h2>%s</h2>" % inline(s[3:])]
        elif cur is None or not s:
            if cur is not None:
                flush_list()
        else:
            m = re.match(r"(-|\d+\.)\s+(.*)", s)
            if m:
                k = "ul" if m.group(1) == "-" else "ol"
                if kind and kind != k:
                    flush_list()
                kind = k
                items.append(inline(m.group(2)))
            elif items:
                items[-1] += " " + inline(s)
            else:
                flush_list()
                cur.append("<p>%s</p>" % inline(s))
    if cur is not None:
        flush_list()
        out.append(cur)
    return "\n".join('    <div class="panel">\n      ' + "\n      ".join(p) + "\n    </div>" for p in out)


def ess_cell(b):
    e = b.get("ess")
    if e is None:
        return "–"
    return '<span class="hi">%d</span>' % e if e < 200 else "{:,}".format(e)


def z_cell(b):
    z = b.get("z")
    if z is None:
        return "–"
    t = "%.3g" % z
    return '<span class="hi">%s</span>' % t if z >= 3 else t


# --------------------------------------------------------------------------------------
# Tracks
# --------------------------------------------------------------------------------------

def beauti_track(batch):
    status = tsv("reports/status.tsv", 3, BEAUTI_STATUSES, ID_RE.fullmatch)
    assign = {}
    for c in md_rows(read("ASSIGNMENTS.md")):
        m = ID_RE.match(c[0]) if c else None
        if not m or len(c) < 7:
            continue
        data, subst, clock, tree, extra = (plain(x) for x in c[2:7])
        if extra and extra not in ("—", "-", "All defaults"):
            data = "%s · %s" % (data, extra)
        assign[m.group(0)] = {"who": plain(c[1]), "model": " · ".join(x for x in (subst, clock, tree) if x), "data": data}
    ids = sorted(set(status) | set(assign))
    msgs = checks({k: v[0] for k, v in status.items()}, batch, BEAUTI_STATUSES)
    for cid in ids:
        if cid not in status:
            msgs.append("%s is in ASSIGNMENTS.md but not in reports/status.tsv." % cid)
        if cid not in assign:
            msgs.append("%s is in reports/status.tsv but not in ASSIGNMENTS.md." % cid)
    rows = []
    for cid in ids:
        st, note = status.get(cid, ("none", ""))
        a, b = assign.get(cid, {}), batch.get(cid, {})
        rows.append({"st": st, "cells": [
            '<td class="id">%s</td>' % cid,
            '<td class="tester">%s</td>' % esc(a.get("who", "")),
            '<td class="model">%s<small>%s</small></td>' % (esc(a.get("model", "")), esc(a.get("data", ""))),
            '<td class="num">%s</td>' % ess_cell(b), '<td class="num">%s</td>' % z_cell(b),
            None, '<td class="note">%s</td>' % inline(note)]})
    return {
        "file": "beauti.html", "title": "BEAUti Track Status", "short": "BEAUti by hand",
        "eyebrow": "BEAUti by hand",
        "h1": "C01–C30: analyses built by hand in BEAUti",
        "lede": "Each combination is built by hand in BEAUti 2.7.9 and BEAUti 3, run with seeds 1 and 2 in both "
                "versions, and compared marginal by marginal. Together the 30 cover every substitution, frequency, "
                "clock, tree-prior and starting-tree option in the BEAST 3 templates.",
        "unit": "combinations", "statuses": BEAUTI_STATUSES, "rows": rows, "checks": msgs,
        "head": ["ID", "Tester", "Model", "Min ESS", "Max z", "Status", "Detail and next step"],
        "num_cols": (3, 4), "min_width": 900, "panels": panels("reports/status-notes.md"),
        "sources": "<code>reports/status.tsv</code> (status and note), <code>reports/status-notes.md</code>, "
                   "<code>reports/summary/batch-summary.md</code> (numbers), <code>ASSIGNMENTS.md</code> (tester, model)",
        "summary": lambda c, n: "<b>%d of %d</b> pass, counting the %d with explained differences. <b>%d of %d</b> agree "
                                "between the versions." % (c("pass", "explained"), n, c("explained"),
                                                           c("pass", "explained", "partial"), n),
    }


def example_run_name(ex):
    base, ext = os.path.splitext(ex)
    return base + "-json" if ext == ".json" else base


def examples_track(batch):
    status = tsv("reports/examples-status.tsv", 4, EXAMPLE_STATUSES, lambda k: bool(re.fullmatch(r"[\w.-]+\.(xml|json)", k)))
    inv = []
    for c in md_rows(read("README.md")):
        if len(c) >= 5 and c[0].isdigit() and re.search(r"\.(xml|json)$", c[1]):
            inv.append({"ex": c[1], "conv": plain(c[2]), "pr": c[3]})
    if not inv:
        sys.exit("README.md: example inventory table not found")
    tested = [r for r in inv if r["conv"] != "excluded"]
    names = set(r["ex"] for r in tested)
    msgs = checks({k: v[1] for k, v in status.items()}, batch, EXAMPLE_STATUSES, example_run_name)
    for ex in sorted(names - set(status)):
        msgs.append("%s is in the README inventory but not in reports/examples-status.tsv." % ex)
    for ex in sorted(set(status) - names):
        msgs.append("%s is in reports/examples-status.tsv but not in the README inventory (or is excluded)." % ex)
    rows = []
    for r in tested:
        who, st, note = status.get(r["ex"], ("", "none", ""))
        b = batch.get(example_run_name(r["ex"]), {})
        rows.append({"st": st, "cells": [
            '<td class="id">%s</td>' % esc(r["ex"]),
            '<td class="tester">%s</td>' % esc(who),
            '<td>%s</td>' % esc(r["conv"]), '<td>%s</td>' % (inline(r["pr"]) or "earlier"),
            '<td class="num">%s</td>' % ess_cell(b), '<td class="num">%s</td>' % z_cell(b),
            None, '<td class="note">%s</td>' % inline(note)]})
    return {
        "file": "examples.html", "title": "Example XML Status", "short": "Example XMLs",
        "eyebrow": "Example XMLs",
        "h1": "The BEAST 2 example XMLs in BEAST 3",
        "lede": "Each example XML shipped with BEAST 2 v2.7.8 is converted to BEAST 3, both are run with seeds 1 and 2, "
                "and the posteriors are compared marginal by marginal. %d examples are tested; the 2 *BEAST 1 "
                "examples are excluded." % len(tested),
        "unit": "examples", "statuses": EXAMPLE_STATUSES, "rows": rows, "checks": msgs,
        "head": ["Example", "Tester", "Converted", "Converted in", "Min ESS", "Max z", "Status", "Detail and next step"],
        "num_cols": (4, 5), "min_width": 960, "panels": panels("reports/examples-notes.md"),
        "sources": "<code>reports/examples-status.tsv</code> (tester, status and note), <code>reports/examples-notes.md</code>, "
                   "<code>reports/summary/batch-summary.md</code> (numbers), <code>README.md</code> (inventory)",
        "summary": lambda c, n: "<b>%d of %d</b> pass, counting the %d with explained differences. <b>%d</b> need a "
                                "decision and <b>%d</b> have not been run yet." % (c("pass", "explained"), n,
                                                                                    c("explained"), c("open"), c("none"), ),
    }


# --------------------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------------------

FILTER_JS = r"""<script>
const S = __STATUSES__;
const R = __ROWS__;
const order = Object.keys(S);
const counts = Object.fromEntries(order.map(k => [k, R.filter(r => r.st === k).length]));
let filter = null;
const strip = document.getElementById("strip");
order.forEach(k => {
  const b = document.createElement("button");
  b.type = "button"; b.id = "tile-" + k; b.className = "tile s-" + k; b.setAttribute("aria-pressed", "false");
  b.innerHTML = `<span class="n">${counts[k]}</span><span class="l">${S[k][0]}</span><span class="d">${S[k][1]}</span>`;
  b.addEventListener("click", () => { filter = filter === k ? null : k; render(); });
  strip.appendChild(b);
});
function render() {
  document.querySelectorAll(".tile").forEach(t => t.setAttribute("aria-pressed", String(t.id === "tile-" + filter)));
  document.getElementById("rows").innerHTML = R.filter(r => !filter || r.st === filter).map(r =>
    `<tr class="s-${r.st}">` + r.cells.map(c => c === null ? `<td><span class="pill">${S[r.st][0]}</span></td>` : c).join("") + "</tr>"
  ).join("");
}
render();
</script>"""


def bar(statuses, rows):
    counts = [(k, sum(r["st"] == k for r in rows)) for k in statuses]
    return '<div class="bar" aria-hidden="true">' + "".join(
        '<span class="s-%s" style="flex:%d"></span>' % (k, n) for k, n in counts if n) + "</div>"


def nav(current, tracks):
    links = [("index.html", "Overview")] + [(t["file"], t["short"]) for t in tracks] + EXTRA_PAGES
    return '  <nav class="nav">' + "".join(
        '<a href="%s"%s>%s</a>' % (f, ' aria-current="page"' if f == current else "", esc(lab)) for f, lab in links) + "</nav>"


def track_page(t, tracks, stamp, footer):
    n = len(t["rows"])
    count = lambda *ks: sum(r["st"] in ks for r in t["rows"])
    heads = "".join('<th class="num">%s</th>' % h if i in t["num_cols"] else "<th>%s</th>" % h for i, h in enumerate(t["head"]))
    check_html = ""
    if t["checks"]:
        check_html = ('  <section class="panel checks">\n    <h2>Status file out of step with the numbers</h2>\n'
                      "    <ul>" + "".join("<li>%s</li>" % esc(m) for m in t["checks"]) + "</ul>\n  </section>\n")
    body = """%s
  <header>
    <div class="eyebrow">BEAST 3 validation · %s · updated %s</div>
    <h1>%s</h1>
    <p class="lede">%s</p>
  </header>
  <section style="display:grid;gap:10px">
    <div class="strip" id="strip"></div>
    %s
    <div class="barnote"><span>%s</span><span>Click a box to filter the table. Click again to show all.</span></div>
  </section>
%s  <section style="display:grid;gap:10px">
    <h2>All %d %s</h2>
    <div class="tablebox">
      <table style="min-width:%dpx">
        <thead><tr>%s</tr></thead>
        <tbody id="rows"></tbody>
      </table>
    </div>
  </section>
  <section class="cols">
%s
  </section>
  <footer>Sources: %s. %s</footer>""" % (
        nav(t["file"], tracks), esc(t["eyebrow"]), stamp, esc(t["h1"]), esc(t["lede"]), bar(t["statuses"], t["rows"]),
        t["summary"](count, n), check_html, n, t["unit"], t["min_width"], heads, t["panels"], t["sources"], footer)
    script = (FILTER_JS.replace("__STATUSES__", json.dumps(t["statuses"], ensure_ascii=False))
              .replace("__ROWS__", json.dumps(t["rows"], ensure_ascii=False).replace("</", "<\\/")))
    return t["title"], body, script


def milestone_data():
    """The milestone snapshot and the hand-set sorting: (snapshot, issue rows, pr rows, messages)."""
    snap = json.loads(read("reports/milestone.json"))
    repo_url = "https://github.com/%s" % snap["repo"]

    def refs(text):
        # #123 on its own is an issue or pull request of the repository
        return re.sub(r'(?<![\w/&">#])#(\d{2,5})\b', r'<a href="%s/issues/\1">#\1</a>' % repo_url, inline(text))

    triage = {}
    for n, line in enumerate(read("reports/milestone-triage.tsv").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = [x.strip() for x in line.split("\t")] + ["", ""]
        if not parts[0].isdigit() or parts[1] not in list(MILESTONE_GROUPS) + ["pr"]:
            sys.exit("reports/milestone-triage.tsv line %d: bad number or group: %r" % (n, line))
        triage[int(parts[0])] = (parts[1], parts[2])

    fixes = {}
    for p in snap["prs"]:
        for c in p["closes"]:
            fixes.setdefault(c, []).append(p)
    link = lambda x: '<a href="%s">#%d</a>' % (x["url"], x["number"])
    seen, msgs, issues = set(), [], []
    for i in snap["issues"]:
        group, note = triage.get(i["number"], ("new", ""))
        seen.add(i["number"])
        if group == "pr":
            msgs.append("#%d is an issue, but milestone-triage.tsv lists it as a pull request." % i["number"])
            group = "new"
        if fixes.get(i["number"]) and group != "review":
            msgs.append("#%d has an open pull request, but is not sorted under 'Fix in review'." % i["number"])
        if group == "review" and not fixes.get(i["number"]):
            msgs.append("#%d is sorted under 'Fix in review', but no open pull request closes it." % i["number"])
        who = ", ".join(i["assignees"]) or "–"
        issues.append({"st": group, "cells": [
            '<td class="id">%s</td>' % link(i),
            '<td class="model">%s<small>opened %s by %s</small></td>' % (esc(i["title"]), i["created"], esc(i["author"])),
            '<td class="tester">%s</td>' % esc(who),
            '<td>%s</td>' % (", ".join(link(p) for p in fixes.get(i["number"], [])) or "–"),
            None, '<td class="note">%s</td>' % refs(note)]})
    order = list(MILESTONE_GROUPS)
    issues.sort(key=lambda r: order.index(r["st"]))

    prs = []
    for p in snap["prs"]:
        seen.add(p["number"])
        checks_cell = {"pass": "pass", "none": "–"}.get(p["checks"], '<span class="hi">%s</span>' % esc(p["checks"]))
        review_cell = esc(p["review"]) if p["review"] == "approved" else '<span class="hi">%s</span>' % esc(p["review"])
        prs.append("<tr>" + "".join([
            '<td class="id">%s</td>' % link(p),
            '<td class="model">%s%s<small>by %s, updated %s</small></td>' % (
                esc(p["title"]), " (draft)" if p["draft"] else "", esc(p["author"]), p["updated"]),
            '<td>%s</td>' % (", ".join('<a href="%s/issues/%d">#%d</a>' % (repo_url, c, c) for c in p["closes"]) or "–"),
            '<td>%s</td>' % (esc(p["milestone"]) or '<span class="hi">none</span>'),
            '<td>%s</td>' % checks_cell, '<td>%s</td>' % review_cell,
            '<td class="note">%s</td>' % refs(triage.get(p["number"], ("pr", ""))[1])]) + "</tr>")
    for n in sorted(set(triage) - seen):
        msgs.append("#%d is in milestone-triage.tsv but is no longer open (or no longer on the milestone)." % n)
    return snap, issues, prs, msgs


def milestone_page(tracks, footer):
    snap, issues, prs, msgs = milestone_data()
    fetched = datetime.datetime.strptime(snap["fetched"], "%Y-%m-%dT%H:%M:%SZ").strftime("%-d %b %Y, %H:%M UTC")
    repo_url = "https://github.com/%s" % snap["repo"]
    count = lambda k: sum(r["st"] == k for r in issues)
    check_html = ""
    if msgs:
        check_html = ('  <section class="panel checks">\n    <h2>Sorting out of step with GitHub</h2>\n'
                      "    <ul>" + "".join("<li>%s</li>" % esc(m) for m in msgs) + "</ul>\n  </section>\n")
    on_ms = sum(1 for p in snap["prs"] if p["milestone"] == snap["milestone"])
    body = """%s
  <header>
    <div class="eyebrow">BEAST 3 release · milestone %s · GitHub as at %s</div>
    <h1>What is left for BEAST %s</h1>
    <p class="lede">The open issues on the <a href="%s/milestones">%s milestone</a> of %s, and every open pull request.
      The grouping and the notes are a suggestion for the meeting, not decisions.</p>
  </header>
%s  <section style="display:grid;gap:10px">
    <h2>%d open pull requests</h2>
    <div class="tablebox">
      <table style="min-width:980px">
        <thead><tr><th>PR</th><th>Title</th><th>Fixes</th><th>Milestone</th><th>CI</th><th>Review</th><th>What it needs</th></tr></thead>
        <tbody>%s</tbody>
      </table>
    </div>
    <div class="barnote"><span><b>%d of %d</b> are on the milestone. None has an approving review.</span></div>
  </section>
  <section style="display:grid;gap:10px">
    <h2>%d open issues on the milestone</h2>
    <div class="strip" id="strip"></div>
    %s
    <div class="barnote"><span><b>%d</b> have a fix in review, <b>%d</b> are ready to be fixed, <b>%d</b> need a decision. %d issue(s) on the milestone are closed.</span><span>Click a box to filter the table. Click again to show all.</span></div>
    <div class="tablebox">
      <table style="min-width:980px">
        <thead><tr><th>Issue</th><th>Title</th><th>Assigned</th><th>PR</th><th>Suggested</th><th>Note</th></tr></thead>
        <tbody id="rows"></tbody>
      </table>
    </div>
  </section>
  <section class="cols">
%s
  </section>
  <footer>Sources: <code>reports/milestone.json</code> (snapshot of GitHub, <code>scripts/fetch_milestone.py</code>),
    <code>reports/milestone-triage.tsv</code> (group and note), <code>reports/milestone-notes.md</code>. %s</footer>""" % (
        nav("milestone.html", tracks), esc(snap["milestone"]), fetched, esc(snap["milestone"]), repo_url,
        esc(snap["milestone"]), esc(snap["repo"]), check_html, len(prs), "\n".join(prs), on_ms, len(prs),
        len(issues), bar(MILESTONE_GROUPS, issues), count("review"), count("todo"), count("decide"), snap["closed"],
        panels("reports/milestone-notes.md"), footer)
    if any(p["review"] == "approved" for p in snap["prs"]):
        body = body.replace(" None has an approving review.", "")
    groups = {k: v for k, v in MILESTONE_GROUPS.items() if k != "new" or count("new")}
    script = (FILTER_JS.replace("__STATUSES__", json.dumps(groups, ensure_ascii=False))
              .replace("__ROWS__", json.dumps(issues, ensure_ascii=False).replace("</", "<\\/")))
    card = """    <a class="card" href="milestone.html">
      <h2>%s milestone →</h2>
      <p>The open issues and pull requests that stand between master and the release, sorted for review.</p>
      <div class="big">%d issues, %d pull requests open</div>
      %s
      <div class="legend">%s</div>
    </a>""" % (esc(snap["milestone"]), len(issues), len(prs), bar(MILESTONE_GROUPS, issues),
               "".join('<span class="s-%s">%d %s</span>' % (k, count(k), esc(v[0].lower()))
                       for k, v in MILESTONE_GROUPS.items() if count(k)))
    return ("BEAST %s Milestone" % snap["milestone"], body, script), card, msgs


def index_page(tracks, stamp, footer, extra_cards=()):
    cards = []
    for t in tracks:
        n = len(t["rows"])
        p = sum(r["st"] in PASSED for r in t["rows"])
        legend = "".join('<span class="s-%s">%d %s</span>' % (k, c, esc(v[0].lower()))
                         for k, v in t["statuses"].items() for c in [sum(r["st"] == k for r in t["rows"])] if c)
        warn = ('<p class="hi">%d status line(s) out of step with the numbers.</p>' % len(t["checks"])) if t["checks"] else ""
        cards.append("""    <a class="card" href="%s">
      <h2>%s →</h2>
      <p>%s</p>
      <div class="big">%d of %d passed</div>
      %s
      <div class="legend">%s</div>
      %s
    </a>""" % (t["file"], esc(t["short"]), esc(t["lede"]), p, n, bar(t["statuses"], t["rows"]), legend, warn))
    body = """%s
  <header>
    <div class="eyebrow">BEAST 3 validation · updated %s</div>
    <h1>Does BEAST 3 sample the same posterior as BEAST 2?</h1>
  </header>
  <section class="prose">
    <p>BEAST 3 (release 2.8.0, due 3 Dec 2026) is a rewrite of BEAST 2's core. Before it is released we check that it gives the same answers as BEAST 2.7.9 on two kinds of analysis:</p>
    <p><b>The example XMLs.</b> Every example shipped with BEAST 2 is converted to BEAST 3 and both are run, which tests the XML-to-MCMC path model by model. The unmodified BEAST 2 XMLs are also loaded in BEAST 3, as a backward-compatibility check.</p>
    <p><b>Analyses built by hand in BEAUti.</b> 30 analyses are built in BEAUti 2.7.9 and BEAUti 3 by five testers, covering every model option in the templates. This tests what users actually do.</p>
    <p>Each analysis runs twice in each version (seeds 1 and 2). Every logged parameter is compared: a z test on the means (flag at z ≥ 3), overlap of the 95%% HPD intervals, ESS ≥ 200, and clade probabilities. A flag that can be traced to a known, harmless difference, such as a constant offset in the log prior, counts as passed, explained.</p>
    <p>Results are collated on Wed 11 Nov and signed off on Fri 13 Nov.</p>
  </section>
  <section class="cards">
%s
  </section>
  <footer>%s Repository: <a href="https://github.com/CompEvol/beast3-test">CompEvol/beast3-test</a>.</footer>""" % (
        nav("index.html", tracks), stamp, "\n".join(cards + list(extra_cards)), footer)
    return "BEAST 3 Validation", body, ""


def commit():
    sha = os.environ.get("GITHUB_SHA")
    if sha:
        return sha[:7]
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=os.path.join(ROOT, "_site"), help="output directory (default _site)")
    args = ap.parse_args()

    batch = load_batch()
    tracks = [examples_track(batch), beauti_track(batch)]
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%-d %b %Y, %H:%M UTC")
    footer = ("Built from commit <code>%s</code> by <code>scripts/build_status_page.py</code>. Min ESS is the lowest ESS "
              "over all logged columns and replicates; max z is the largest standardised difference between the "
              "BEAST 2 and BEAST 3 means." % commit())
    layout = read("scripts/status_page.html")
    os.makedirs(args.out, exist_ok=True)
    ms_page, ms_card, ms_msgs = milestone_page(tracks, "Built from commit <code>%s</code> by "
                                               "<code>scripts/build_status_page.py</code>." % commit())
    pages = ([("index.html", index_page(tracks, stamp, footer, [ms_card]))]
             + [(t["file"], track_page(t, tracks, stamp, footer)) for t in tracks] + [("milestone.html", ms_page)])
    for fname, (title, body, script) in pages:
        page = layout.replace("__TITLE__", title).replace("__BODY__", body).replace("__SCRIPT__", script)
        with open(os.path.join(args.out, fname), "w", encoding="utf-8") as f:
            f.write(page)
    for t in tracks:
        print("%s: %d %s, %d check(s)" % (t["file"], len(t["rows"]), t["unit"], len(t["checks"])))
        for m in t["checks"]:
            print("  check:", m)
    print("milestone.html: %d check(s)" % len(ms_msgs))
    for m in ms_msgs:
        print("  check:", m)
    print("wrote %s" % args.out)


if __name__ == "__main__":
    main()
