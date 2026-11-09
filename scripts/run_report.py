#!/usr/bin/env python3
"""Markdown report for the replicate runs made by scripts/run_examples.sh.

For every example and replicate: completed or not (exit code, exceptions in beast.out, and for
MCMC runs the final "End likelihood" line), the seed, wall time and the minimum ESS over all
numeric columns of all trace logs (*.log) in the rep directory, after burn-in. ESS is computed
with compare.py's ess(), which matches LogAnalyser. Failed runs are listed at the top.
"""

import argparse
import datetime
import glob
import math
import os
import platform
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compare import TraceLog, ess  # noqa: E402

ESS_MIN = 200
ERR = re.compile(r"(Exception|Error\b|ERROR|Caused by|could not|Could not)")


def read(path, default=None):
    try:
        with open(path, errors="replace") as fh:
            return fh.read().strip()
    except OSError:
        return default


def cmd(args, cwd=None):
    try:
        p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=60)
        return p.stdout.strip() or p.stderr.strip()
    except Exception as e:  # noqa: BLE001
        return "unknown (%s)" % e


def is_mcmc(model_file):
    txt = read(model_file, "") or ""
    return bool(re.search(r"""spec\s*[=:]\s*["'](beast\.base\.inference\.)?MCMC["']""", txt))


def rep_status(rep_dir, model_file):
    """-> (status, message); status is completed / FAILED / not run."""
    out = read(os.path.join(rep_dir, "beast.out"))
    if out is None:
        return "not run", "no beast.out"
    errtxt = read(os.path.join(rep_dir, "beast.err"), "") or ""
    lines = [l for l in (out + "\n" + errtxt).splitlines() if l.strip()]
    err = None
    for k, l in enumerate(lines):
        if ERR.search(l):
            err = l.strip()
            if re.search(r"parsing the (xml|json)", l) and k + 1 < len(lines):
                err += " — " + lines[k + 1].strip()
                if "type mismatch" in lines[k + 1] and k + 2 < len(lines):
                    err += " " + lines[k + 2].strip()
                cls = next((m.group(1) for m in (re.search(r"spec=['\"]([\w.]+)['\"]", x)
                                                 for x in lines[k + 1:k + 8][::-1]) if m), None)
                if cls:
                    err += " (`%s`)" % cls
            break
    if err:
        return "FAILED", err
    if model_file and is_mcmc(model_file) and "End likelihood" not in out + errtxt:
        return "FAILED", "no final 'End likelihood' line (incomplete or still running?)"
    return "completed", ""


def rep_min_ess(rep_dir, burnin):
    """-> (min ess, column, file, n samples) over all trace logs, or None if there are none."""
    best = None
    for path in sorted(glob.glob(os.path.join(rep_dir, "*.log"))):
        try:
            tl = TraceLog(path, burnin)
        except Exception:  # noqa: BLE001
            continue
        for col, vals in tl.columns.items():
            e = ess(vals)
            if math.isnan(e):
                continue  # constant column
            if best is None or e < best[0]:
                best = (e, col, os.path.basename(path), tl.n)
    return best


def fmt_ess(e):
    if e is None:
        return "n/a"
    s = "%.0f" % e
    return s + " ⚠" if e < ESS_MIN else s


BEASTFX_LEGACY_NOTE = """\
## beast-fx legacy XMLs: deprecated SiteModel in the sequence simulators (fixed on master)

`testSeqGen.xml` and `testSimulatedAlignment.xml` come from
`beast-fx/src/test/resources/beast.fx/examples/legacy/` in the beast3 repo. They run
`beastfx.app.seqgen.SequenceSimulator` and `beastfx.app.seqgen.SimulatedAlignment`, with the deprecated
BEAST 2 site model written by its full name, `beast.base.evolution.sitemodel.SiteModel`.

| Version | Result |
|---|---|
| BEAST 2.7.9 | ✅ Both run (4/4 above). |
| BEAST 3, master | ✅ Both parse after the fix below. |
| BEAST 3, 2.8.0-rc2 app (built 5 Nov) | ❌ Both fail while the XML is loaded. The app predates the fix. |

**Problem:** the rc2 app fails with
`Input 102: type mismatch for input siteModel ... expected class beast.base.spec.evolution.sitemodel.SiteModel`.
The simulators' `siteModel` input was declared as `Input<SiteModel>`, using the BEAST 3 class
(`SequenceSimulator.java:26/39`, `SimulatedAlignment.java:17/30`). The old and new `SiteModel` are
siblings under `SiteModelInterface.Base`, so `Input.java:514` rejected the old one.

**Fix (on master):** both inputs are now `Input<SiteModelInterface.Base>`, which accepts either class.
The cast at `SequenceSimulator.java:304` uses the same type. beast-fx's `testLegacyExamplesParse`
passes again. Details are in `beast-fx/src/test/resources/beast.fx/examples/legacy/README.md` in the
beast3 repo.
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--logroot", required=True)
    ap.add_argument("--status", required=True, help="example<TAB>source list written by the run script")
    ap.add_argument("--beast3", required=True, help="beast3 repo")
    ap.add_argument("--launcher", default="")
    ap.add_argument("--side", default="beast3", choices=["beast2", "beast3"])
    ap.add_argument("--opts", default="")
    ap.add_argument("--burnin", type=int, default=10)
    ap.add_argument("--nrep", type=int, default=4)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    # example, source, then recorded columns named by the header (beast3_branch, beast3_commit,
    # beast_base, java, run_date), taken from the reps' run_info.txt. Older status files have no
    # header and only the first two columns.
    keys = ("beast3_branch", "beast3_commit", "beast_base", "java", "run_date")
    examples, recorded, header = [], {k: {} for k in keys}, None
    with open(a.status) as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if not line.strip():
                continue
            if f[0] == "example":
                header = f
                continue
            name, src = f[0], f[1]
            examples.append((name, src))
            for k, v in zip(header or [], f):
                if k in recorded:
                    for x in filter(None, v.split(",")):
                        recorded[k].setdefault(x, []).append(name)

    rows, failed, summary = [], [], []
    for name, src in examples:
        if src == "MISSING":
            failed.append((name, "-", "-", "source XML/JSON not found in beast-base or beast-fx examples"))
            summary.append((name, "**missing**", "-", "0/%d" % a.nrep, "n/a", ""))
            continue
        model = os.path.basename(src)
        reps = sorted(glob.glob(os.path.join(a.logroot, name, "rep*")),
                      key=lambda p: int(re.sub(r"\D", "", os.path.basename(p)) or 0))
        kind = "MCMC" if is_mcmc(src) else "simulator"
        n_ok, ex_min = 0, None
        for rd in reps:
            rep = os.path.basename(rd)
            status, msg = rep_status(rd, os.path.join(rd, model))
            out = read(os.path.join(rd, "beast.out"), "") or ""
            m = re.search(r"Random number seed: *(\d+)", out)
            seed = m.group(1) if m else "?"
            m = re.search(r"Total calculation time: *([\d.]+)", out)
            secs = "%.0f" % float(m.group(1)) if m else ""
            me = rep_min_ess(rd, a.burnin) if status == "completed" else None
            if status == "completed":
                n_ok += 1
                if me and (ex_min is None or me[0] < ex_min[0]):
                    ex_min = (me[0], me[1], rep)
            else:
                failed.append((name, rep, seed, msg))
            rows.append((name, rep, seed, status, secs, me, msg))
        if not reps:
            failed.append((name, "-", "-", "no replicate directories (not run)"))
        note = "%s in %s" % (ex_min[1], ex_min[2]) if ex_min else ""
        summary.append((name, "`%s`" % src, kind, "%d/%d" % (n_ok, max(a.nrep, len(reps))),
                        fmt_ess(ex_min[0] if ex_min else None), note))

    commit = cmd(["git", "log", "-1", "--format=%h %ad %s", "--date=short"], cwd=a.beast3)
    branch = cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=a.beast3)
    dirty = cmd(["git", "status", "--porcelain", "--untracked-files=no"], cwd=a.beast3)
    ver = cmd([a.launcher, "-version"]).splitlines() if a.launcher else []
    java = [l.replace("Java version", "").strip() for l in ver if l.startswith("Java version")] \
        or [l for l in cmd(["java", "-version"]).splitlines() if "JAVA_TOOL_OPTIONS" not in l]
    pkgs = [l.strip() for l in ver if re.match(r"^\S+ v\d", l.strip())]
    out = []
    w = out.append
    w("# BEAST %s example runs\n" % a.side[-1])
    w("Generated %s by `scripts/run_examples.sh %s`.\n" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), a.side))
    vers = dict(re.match(r"^(\S+) v(\S+)", p).groups() for p in pkgs)

    def recorded_line(key, fallback):
        """'25.0.2', or '25.0.2 (ex1, ex2); 17.0.5 (ex3)' when the examples differ; else fallback."""
        vals = {v: n for v, n in recorded[key].items() if v != "unknown"}
        if not vals:
            return fallback
        if len(vals) == 1:
            return next(iter(vals))
        return "; ".join("%s (%s)" % (v, ", ".join(n)) for v, n in vals.items())

    if recorded["beast_base"]:
        vers["BEAST.base"] = recorded_line("beast_base", vers.get("BEAST.base", "?"))
    if a.side == "beast2":
        w("> **These are BEAST 2 runs with BEAST.base %s** (BEAST.app %s), started by the launcher of the "
          "app installed as \"BEAST 2.7.7\". They are **not** BEAST 3 (2.8.0) runs. The XMLs are the BEAST 2 "
          "versions from the `legacy/` folders, the baseline for the BEAST 3 runs in "
          "`reports/beast3-run-report.md`.\n" % (vers.get("BEAST.base", "?"), vers.get("BEAST.app", "?")))

    w("## Failed runs\n")
    if failed:
        w("| Example | Rep | Seed | Error |")
        w("|---|---|---|---|")
        for name, rep, seed, msg in failed:
            w("| %s | %s | %s | %s |" % (name, rep, seed, msg.replace("|", "\\|")[:300]))
    else:
        w("None — every replicate completed.")
    w("")

    if a.side == "beast2":
        w(BEASTFX_LEGACY_NOTE)

    w("## Setup\n")
    w("- Launcher: `%s`%s" % (a.launcher, " (`-version`: %s)" % ", ".join(pkgs) if pkgs else ""))
    w("- BEAST options: `%s -seed <seed>`" % a.opts)
    app = os.path.dirname(os.path.dirname(os.path.realpath(a.launcher))) if a.launcher else ""
    zips = sorted(glob.glob(os.path.join(app, "BEAST.app", "Contents", "app", "packages", "*.zip")))
    for z in zips:
        w("- Bundled package (seeded into the package dir): `%s`, dated %s"
          % (os.path.basename(z), datetime.datetime.fromtimestamp(os.path.getmtime(z)).strftime("%Y-%m-%d %H:%M")))
    where = "%sexamples of `%s`" % ("`legacy/` folders of the " if a.side == "beast2" else "", a.beast3)
    if recorded["beast3_branch"] or recorded["beast3_commit"]:
        # recorded by copy_examples.sh when the XMLs were copied, so it is what the runs used
        cm = recorded_line("beast3_commit", "unknown").replace("+uncommitted", " (**uncommitted changes**)").replace(
            "+edited", " (edited after copying)")
        w("- XMLs: copied by `scripts/copy_examples.sh` into `%s/xml/` from the %s (branch `%s`, commit %s)"
          % (a.side, where, recorded_line("beast3_branch", "unknown"), cm))
    else:
        w("- XMLs: copied by `scripts/copy_examples.sh` into `%s/xml/` from the %s. Not recorded with the runs; "
          "the beast3 repo is now at branch `%s`, commit %s%s" % (a.side, where, branch, commit,
                                                                 " (**uncommitted changes**)" if dirty else ""))
    java_now = (java[0] if java else "unknown") + " (not recorded with the runs; this is what the launcher uses now)"
    w("- Java: %s" % recorded_line("java", java_now))
    if recorded["run_date"]:
        w("- Run date: %s" % recorded_line("run_date", "unknown"))
    w("- Machine: %s %s (%s)" % (platform.system(), platform.release(), platform.machine()))
    w("- Replicates: %d per example, seed per replicate in `beast.out`, the same as the other version's rep when that ran first" % a.nrep)
    w("- ESS: minimum over all non-constant columns of all `*.log` files in a replicate, "
      "%d %% burn-in; ⚠ = below %d\n" % (a.burnin, ESS_MIN))

    w("## Summary\n")
    w("| Example | Source | Type | Completed | Min ESS | Lowest column |")
    w("|---|---|---|---|---|---|")
    for r in summary:
        w("| %s | %s | %s | %s | %s | %s |" % r)
    w("")

    w("## Replicates\n")
    w("| Example | Rep | Seed | Status | Run time (s) | Samples | Min ESS | Column (file) |")
    w("|---|---|---|---|---|---|---|---|")
    for name, rep, seed, status, secs, me, msg in rows:
        st = status if status == "completed" else "**%s**" % status
        if me:
            w("| %s | %s | %s | %s | %s | %d | %s | %s (%s) |"
              % (name, rep, seed, st, secs, me[3], fmt_ess(me[0]), me[1], me[2]))
        else:
            w("| %s | %s | %s | %s | %s | - | n/a | |" % (name, rep, seed, st, secs))
    w("")

    text = "\n".join(out)
    home = os.path.expanduser("~")
    text = text.replace(os.getcwd() + os.sep, "").replace(home, "~")   # never save absolute paths
    with open(a.out, "w") as fh:
        fh.write(text)
    print("report: %s  (%d failed)" % (a.out, len(failed)))


if __name__ == "__main__":
    main()
