#!/usr/bin/env python3
"""Write the Markdown report of packages/check_packages.sh from the TSV files in its work folder.

Standard library only. Exit status 1 when the new BEAST 3 version fails where the baseline
passes (a regression) or when a package does not build or fails its unit tests; 0 otherwise.
"""

import argparse
import os
import re
import sys
from collections import OrderedDict


def rows(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as fh:
        return [line.rstrip("\n").split("\t") for line in fh if line.strip()]


def tests_ok(text):
    m = re.search(r"Failures: (\d+), Errors: (\d+)", text)
    return m is None or (m.group(1) == "0" and m.group(2) == "0")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--work", required=True)
    ap.add_argument("--out", required=True)
    opts = ap.parse_args()
    w = opts.work

    v = OrderedDict((r[0], r[1]) for r in rows(os.path.join(w, "versions.tsv")) if len(r) > 1)
    new, base = v.get("new", "new"), v.get("baseline", "baseline")
    regressions, known, broken_builds = [], [], []
    out = []
    add = out.append

    add("# Package check")
    add("")
    add("Written by `packages/check_packages.sh`; do not edit by hand. "
        "See [packages/README.md](../packages/README.md) for what is tested and how to read this.")
    add("")
    add("| | |")
    add("|---|---|")
    add("| Date | %s |" % v.get("date", ""))
    add("| New | BEAST %s, beast3 branch `%s`, commit `%s` |" % (new, v.get("beast3_branch", ""), v.get("beast3_commit", "")))
    add("| Baseline | BEAST %s from Maven Central |" % base)
    add("| Java | %s |" % v.get("java", ""))
    add("| Machine | %s |" % v.get("os", ""))
    add("| Example runs | %s replicate(s) per version in the last run, %s at a time; an example run with `-e` may have more (column Finished) |"
        % (v.get("replicates", ""), v.get("jobs", "")))
    add("")

    # ---- build -----------------------------------------------------------------------------
    build = rows(os.path.join(w, "build.tsv"))
    if build:
        add("## Build and unit tests against BEAST %s" % new)
        add("")
        add("Each package's default branch, built from source.")
        add("")
        add("| Package | Repository | Commit | Version | Builds | Unit tests |")
        add("|---|---|---|---|---|---|")
        for r in build:
            r += [""] * (7 - len(r))
            name, repo, commit, built, tests, pkgname, pkgversion = r[:7]
            ok = built == "yes" and tests_ok(tests)
            if not ok:
                broken_builds.append(name)
            add("| %s | [%s](https://github.com/%s) | `%s` | %s | %s | %s |"
                % (pkgname if pkgname not in ("", "–") else name, repo, repo, commit, pkgversion,
                   "yes" if built == "yes" else "**NO**", tests if tests_ok(tests) else "**%s**" % tests))
        add("")

    # ---- examples --------------------------------------------------------------------------
    ex = rows(os.path.join(w, "examples.tsv"))
    cmp_ = OrderedDict((r[0], r[1:]) for r in rows(os.path.join(w, "compare.tsv")))
    if ex:
        add("## Example XMLs: BEAST %s against %s" % (new, base))
        add("")
        add("Each example is run with both versions, same seeds, and the posteriors are compared with "
            "`scripts/compare.py` (10% burn-in, flag z ≥ 3, fail z ≥ 4). \"ESS < 200\" in a verdict means "
            "the chain was too short for some parameter, not that the versions disagree.")
        add("")
        add("| Example | Package | Chain | Finished (%s) | Finished (%s) | Time, s (%s) | Time, s (%s) | Verdict | Detail |"
            % (base, new, base, new))
        add("|---|---|---:|---|---|---:|---:|---|---|")
        names = OrderedDict()
        for r in ex:
            r += [""] * (7 - len(r))
            names.setdefault(r[0], {"pkg": r[1], "chain": r[2], "base": [], "new": []})[r[3]].append((r[5], r[6]))

        def fin(reps):
            return "%d/%d" % (sum(1 for f, _ in reps if f == "yes"), len(reps))

        def secs(reps):
            t = [float(s) for _, s in reps if re.match(r"^[0-9.]+$", s or "")]
            return "%.0f" % (sum(t) / len(t)) if t else "–"

        for name, d in names.items():
            verdict = cmp_.get(name, ["not compared", ""])
            nb = all(f == "yes" for f, _ in d["base"]) and d["base"]
            nn = all(f == "yes" for f, _ in d["new"]) and d["new"]
            vtext = verdict[0]
            # same seeds and the same numbers: no change since the baseline touched this example
            if len(verdict) > 1 and re.search(r"max z: 0;", verdict[1]) and nb and nn:
                vtext = "identical"
            bad_verdict = vtext.startswith("not matched") or vtext.startswith("NOT")
            if not nn or (bad_verdict and nb):
                (regressions if nb else known).append("example `%s` (%s): %s" % (
                    name, d["pkg"], "does not finish with %s" % new if not nn else "posterior differs: %s" % vtext))
            add("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
                name, d["pkg"], d["chain"], fin(d["base"]), fin(d["new"]), secs(d["base"]), secs(d["new"]),
                "**%s**" % vtext if bad_verdict else vtext,
                (verdict[1] if len(verdict) > 1 else "").replace("|", "\\|")))
        add("")
        add("The full comparison of each example is in the work folder, `summary/<example>.md`.")
        add("")

    # ---- beauti ----------------------------------------------------------------------------
    be = rows(os.path.join(w, "beauti.tsv"))
    if be:
        add("## BEAUti with all packages installed")
        add("")
        add("Each scenario (`packages/scenarios.sh`) starts BEAUti, sets the model up as a user would, saves the "
            "XML and runs it for 200,000 steps. \"yes\" means BEAUti finished the steps without an exception, "
            "wrote the XML, and BEAST ran it to the end.")
        add("")
        add("| Scenario | %s | %s | Problem |" % (base, new))
        add("|---|---|---|---|")
        sc = OrderedDict()
        for r in be:
            r += [""] * (6 - len(r))
            sc.setdefault(r[0], {})[r[1]] = r[2:6]

        def cell(x):
            if x is None:
                return "not run", False
            gui, saved, ran, _ = x
            if gui == "yes" and saved == "yes" and ran == "yes":
                return "yes", True
            if gui != "yes":
                return "**BEAUti fails**", False
            if saved != "yes":
                return "**no XML**", False
            return "**XML does not run**", False

        for name, d in sc.items():
            cb, okb = cell(d.get("base"))
            cn, okn = cell(d.get("new"))
            why = (d.get("new") or ["", "", "", ""])[3] if not okn else ""
            if not okn:
                (regressions if okb else known).append("BEAUti scenario `%s`: %s" % (name, why or cn.strip("*")))
            add("| %s | %s | %s | %s |" % (name, cb, cn, why.replace("|", "\\|")))
        add("")

    # ---- trees: TreeAnnotator with CCD ------------------------------------------------------
    tr = rows(os.path.join(w, "trees.tsv"))
    if tr:
        add("## TreeAnnotator with the CCD package")
        add("")
        add("Both versions summarise the same tree file (`examples/new/bModelTest/rep1/dna.trees`) with the CCD "
            "package's point estimates and, as a control, MCC. \"Identical\" compares the summary trees, "
            "ignoring comment lines.")
        add("")
        add("| Method | Runs (%s) | Runs (%s) | Identical |" % (base, new))
        add("|---|---|---|---|")
        for r in tr:
            r += [""] * (4 - len(r))
            method, rb, rn, same = r[:4]
            if rn != "yes":
                (regressions if rb == "yes" else known).append("TreeAnnotator `%s` does not run with %s" % (method, new))
            elif same == "no":
                regressions.append("TreeAnnotator `%s`: the summary tree differs from %s's" % (method, base))
            add("| %s | %s | %s | %s |" % (method, rb, rn, "**no**" if same == "no" else same))
        add("")

    # ---- summary, placed at the top ---------------------------------------------------------
    head = []
    if broken_builds or regressions:
        head.append("**Result: FAILED.**")
    else:
        head.append("**Result: no regressions.**" + (" %d known problem(s), also present in %s." % (len(known), base) if known else ""))
    head.append("")
    if broken_builds:
        head.append("Packages that do not build or fail their unit tests against BEAST %s:" % new)
        head.append("")
        head += ["- %s" % b for b in broken_builds] + [""]
    if regressions:
        head.append("Regressions (fail with %s, pass with %s):" % (new, base))
        head.append("")
        head += ["- %s" % r for r in regressions] + [""]
    if known:
        head.append("Known problems (fail with both versions, so not caused by changes since %s):" % base)
        head.append("")
        head += ["- %s" % k for k in known] + [""]
    text = "\n".join(out[:4] + head + out[4:]) + "\n"

    os.makedirs(os.path.dirname(os.path.abspath(opts.out)), exist_ok=True)
    with open(opts.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("\n".join(head))
    return 1 if (broken_builds or regressions) else 0


if __name__ == "__main__":
    sys.exit(main())
