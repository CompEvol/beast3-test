#!/usr/bin/env python3
"""Build the BEAUti-track status page (GitHub Pages) from files in the repo.

Inputs:
  reports/status.tsv               hand-edited status and note per combination
  reports/status-notes.md          hand-edited panels shown under the table
  reports/summary/batch-summary.md min ESS, max z and verdict per combination (compare.py --all)
  ASSIGNMENTS.md                   tester and model per combination
  scripts/status_page.html         page template

Usage: scripts/build_status_page.py [--out _site/index.html]

The page also lists checks where the status file and the numbers disagree. These are printed too.
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

STATUSES = {
    "pass": ["Passed", "Matched, no flags, full chains"],
    "explained": ["Passed, explained", "Flag due to a known difference"],
    "partial": ["Matched, runs short", "Most runs stopped early"],
    "rerun": ["Rerun needed", "rc1 build or a flag to recheck"],
    "blocked": ["Needs rc3", "Fix landed after rc2"],
    "fail": ["Not matched", "Unexplained difference"],
    "none": ["Not run yet", "No results in the repo"],
}
ID_RE = re.compile(r"C\d{2}")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def inline(text):
    """Escape text and convert `code` and **bold**."""
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)
    return out


def plain(md):
    """Strip markdown links, bold and backticks from a table cell."""
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    return md.replace("**", "").replace("`", "").strip()


def table_rows(text):
    """Yield the cells of markdown table rows whose first cell starts with a combination ID."""
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        m = ID_RE.match(cells[0]) if cells else None
        if m:
            yield m.group(0), cells


def load_status():
    rows = {}
    for n, line in enumerate(read("reports/status.tsv").splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        cid, status = parts[0].strip(), parts[1].strip() if len(parts) > 1 else ""
        if not ID_RE.fullmatch(cid) or status not in STATUSES:
            sys.exit(f"reports/status.tsv line {n}: expected 'CNN<TAB>status<TAB>note', "
                     f"status one of {', '.join(STATUSES)}: {line!r}")
        if cid in rows:
            sys.exit(f"reports/status.tsv line {n}: {cid} listed twice")
        rows[cid] = (status, parts[2].strip() if len(parts) > 2 else "")
    return rows


def load_assignments():
    out = {}
    for cid, c in table_rows(read("ASSIGNMENTS.md")):
        if len(c) < 7:
            continue
        data, subst, clock, tree, extra = (plain(x) for x in c[2:7])
        model = " · ".join(x for x in (subst, clock, tree) if x)
        if extra and extra not in ("—", "-", "All defaults"):
            data = f"{data} · {extra}"
        out[cid] = {"who": plain(c[1]), "model": model, "data": data}
    return out


def num(cell, kind):
    try:
        return kind(cell)
    except ValueError:
        return None


def load_batch():
    """Combination rows of batch-summary.md: Name | Reps | Min ESS | Max z | Max clade | Flagged | Verdict."""
    out = {}
    for cid, c in table_rows(read("reports/summary/batch-summary.md")):
        if c[0] != cid or len(c) < 7:   # skip variants such as C01-slide
            continue
        out[cid] = {"ess": num(c[2], int), "z": num(c[3], float), "verdict": c[6]}
    return out


def checks(status, batch):
    msgs = []
    for cid, (st, _) in sorted(status.items()):
        b = batch.get(cid)
        if st == "none":
            if b:
                msgs.append(f"{cid} is marked not run, but batch-summary.md has results ({b['verdict']}).")
            continue
        if not b:
            msgs.append(f"{cid} is marked {STATUSES[st][0].lower()}, but batch-summary.md has no row for it.")
            continue
        if st in ("pass", "partial"):
            if not b["verdict"].startswith("matched"):
                msgs.append(f"{cid} is marked {STATUSES[st][0].lower()}, but the latest verdict is '{b['verdict']}'.")
            if b["z"] is not None and b["z"] >= 3:
                msgs.append(f"{cid} is marked {STATUSES[st][0].lower()}, but max z is {b['z']:g}.")
        if st == "pass" and b["ess"] is not None and b["ess"] < 200:
            msgs.append(f"{cid} is marked passed, but min ESS is {b['ess']}.")
    return msgs


def panels():
    text = re.sub(r"<!--.*?-->", "", read("reports/status-notes.md"), flags=re.S)
    out, cur, items, kind = [], None, [], None

    def flush_list():
        nonlocal items, kind
        if items:
            cur.append(f"<{kind}>" + "".join(f"<li>{i}</li>" for i in items) + f"</{kind}>")
        items, kind = [], None

    for line in text.splitlines():
        s = line.strip()
        if s.startswith("## "):
            if cur is not None:
                flush_list()
                out.append(cur)
            cur = [f"<h2>{inline(s[3:])}</h2>"]
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
                cur.append(f"<p>{inline(s)}</p>")
    if cur is not None:
        flush_list()
        out.append(cur)
    return "\n".join('    <div class="panel">\n      ' + "\n      ".join(p) + "\n    </div>" for p in out)


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
    ap.add_argument("--out", default=os.path.join(ROOT, "_site", "index.html"))
    args = ap.parse_args()

    status, assign, batch = load_status(), load_assignments(), load_batch()
    ids = sorted(set(status) | set(assign))
    msgs = checks(status, batch)
    for cid in ids:
        if cid not in status:
            msgs.append(f"{cid} is in ASSIGNMENTS.md but not in reports/status.tsv.")
        if cid not in assign:
            msgs.append(f"{cid} is in reports/status.tsv but not in ASSIGNMENTS.md.")

    rows = []
    for cid in ids:
        st, note = status.get(cid, ("none", ""))
        a, b = assign.get(cid, {}), batch.get(cid, {})
        z = b.get("z")
        rows.append({"id": cid, "who": html.escape(a.get("who", "")),
                     "model": html.escape(a.get("model", "")), "data": html.escape(a.get("data", "")),
                     "ess": b.get("ess"), "z": None if z is None else f"{z:.3g}",
                     "st": st, "note": inline(note)})

    count = lambda *ks: sum(r["st"] in ks for r in rows)
    total = len(rows)
    summary = (f"<b>{count('pass', 'explained')} of {total}</b> pass, counting the "
               f"{count('explained')} with explained differences. "
               f"<b>{count('pass', 'explained', 'partial')} of {total}</b> agree between the versions.")
    check_html = ""
    if msgs:
        check_html = ('  <section class="panel checks">\n    <h2>Status file out of step with the numbers</h2>\n'
                      '    <ul>' + "".join(f"<li>{html.escape(m)}</li>" for m in msgs) + "</ul>\n"
                      "    <p>Update <code>reports/status.tsv</code> to match the latest reports.</p>\n  </section>\n")
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%-d %b %Y, %H:%M UTC")
    sha = commit()
    footer = (f"Built from commit <code>{sha}</code> of CompEvol/beast3-test by "
              "<code>scripts/build_status_page.py</code>. Status and notes: <code>reports/status.tsv</code>; "
              "numbers: <code>reports/summary/batch-summary.md</code>; tester and model: "
              "<code>ASSIGNMENTS.md</code>. Min ESS is the lowest ESS over all logged columns and replicates; "
              "max z is the largest standardised difference between the BEAST 2 and BEAST 3 means.")

    page = read("scripts/status_page.html")
    for key, val in {"__UPDATED__": now, "__SUMMARY__": summary, "__CHECKS__": check_html,
                     "__TOTAL__": str(total), "__PANELS__": panels(), "__FOOTER__": footer,
                     "__STATUSES__": json.dumps(STATUSES, ensure_ascii=False),
                     "__ROWS__": json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")}.items():
        page = page.replace(key, val)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"wrote {args.out}: {total} combinations, {len(msgs)} check(s)")
    for m in msgs:
        print("  check:", m)


if __name__ == "__main__":
    main()
