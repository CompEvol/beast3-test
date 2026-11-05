#!/usr/bin/env python3
"""Compare BEAST posteriors between two sets of runs (BEAST 2.7.9 vs BEAST 3).

Standard library only (Python >= 3.8). matplotlib is used only with --plots.

Typical use (from the repository root):

    python3 scripts/compare.py beauti-C07          # beast2/log/beauti-C07 vs beast3/log/beauti-C07
    python3 scripts/compare.py testHKY -b 10       # example-XML track, 10 % burn-in
    python3 scripts/compare.py --all               # every <name> present in both versions
    python3 scripts/compare.py --name C30-resume \\
        --a beast3/log/beauti-C30-resumed --label-a resumed \\
        --b beast3/log/beauti-C30 --label-b uninterrupted

Statistics follow BEAST's LogAnalyser (beastfx.app.tools.LogAnalyser) exactly:
burn-in = floor(lines * b / 100) log lines per replicate; mean; sd with divisor n;
95 % HPD = Tracer's shortest interval covering floor((n-1)*0.95)+1 sorted samples;
ESS = BEAST/Tracer autocorrelation ESS (beast.base.spec.inference.util.ESS.ACT,
max lag min(n, 2000), stop at the first even lag where AC[lag-1] + AC[lag] <= 0).

Replicates of one version are combined by concatenating their post-burn-in samples
(mean, sd and HPD of the pooled samples); the ESS of the combination is the SUM of
the per-replicate ESS values (computing the ESS of a concatenated trace would treat
the join between replicates as part of one chain).
"""

import argparse
import difflib
import fnmatch
import glob
import itertools
import math
import operator
import os
import re
import sys
from collections import Counter, OrderedDict

MAX_LAG = 2000
NAN = float("nan")

_sumprod = getattr(math, "sumprod", None)  # Python >= 3.12


def _dot(a, b):
    if _sumprod is not None:
        return _sumprod(a, b)
    return sum(map(operator.mul, a, b))


def isnan(x):
    return x is None or (isinstance(x, float) and math.isnan(x))


# --------------------------------------------------------------------------------------
# Statistics
# --------------------------------------------------------------------------------------

def ess(x):
    """Effective sample size exactly as BEAST's ESS.ACT / LogAnalyser computes it.

    The autocorrelation at each lag is evaluated lazily, only up to the lag where
    BEAST's stopping rule fires, so the result equals evaluating all lags up to
    min(n, 2000) first. Returns NaN for a constant trace (BEAST gives NaN too)."""
    n = len(x)
    if n < 2:
        return NAN
    total = sum(x)
    mean = total / n
    head = [0.0] + list(itertools.accumulate(x))          # head[k] = sum(x[:k])
    max_lag = min(n, MAX_LAG)

    def ac(lag):
        sls = _dot(x[:n - lag], x[lag:])
        sum1 = total - (head[n] - head[n - lag])   # total minus the last `lag` values
        sum2 = total - head[lag]                   # total minus the first `lag` values
        return (sls - (sum1 + sum2) * mean + mean * mean * (n - lag)) / (n - lag)

    ac0 = ac(0)
    if not ac0 > 0:
        return NAN
    integral = ac0
    for lag in range(2, max_lag, 2):
        s = ac(lag - 1) + ac(lag)
        if s > 0:
            integral += 2.0 * s
        else:
            break
    return n / (integral / ac0)


class Stats(object):
    __slots__ = ("n", "mean", "sd", "lo", "hi", "ess", "nreps")

    def __init__(self, n=0, mean=NAN, sd=NAN, lo=NAN, hi=NAN, ess=NAN, nreps=1):
        self.n, self.mean, self.sd, self.lo, self.hi, self.ess, self.nreps = n, mean, sd, lo, hi, ess, nreps

    @property
    def constant(self):
        return self.n > 0 and self.sd == 0

    @property
    def se(self):
        if self.constant:
            return 0.0
        if isnan(self.ess) or self.ess <= 0:
            return NAN
        return self.sd / math.sqrt(self.ess)


def summarise(values, with_ess=True):
    n = len(values)
    if n == 0:
        return Stats()
    s = sum(values)
    s2 = sum(v * v for v in values)
    mean = s / n
    sd = math.sqrt(max(0.0, s2 / n - mean * mean))
    srt = sorted(values)
    k = int((n - 1) * 95.0 / 100.0)
    best, idx = float("inf"), 0
    for i in range(n - k):
        r = srt[i + k] - srt[i]
        if r < best:
            best, idx = r, i
    if srt[0] == srt[-1]:
        sd = 0.0
    e = ess(values) if (with_ess and sd > 0) else NAN
    return Stats(n, mean, sd, srt[idx], srt[idx + k], e)


def combine(rep_values, rep_stats):
    pooled = []
    for v in rep_values:
        pooled.extend(v)
    st = summarise(pooled, with_ess=False)
    esses = [r.ess for r in rep_stats]
    st.ess = NAN if any(isnan(e) for e in esses) else sum(esses)
    st.nreps = len(rep_stats)
    return st


def zstat(a, b):
    d = abs(a.mean - b.mean)
    sa, sb = a.se, b.se
    if isnan(sa) or isnan(sb):
        return NAN
    s = math.sqrt(sa * sa + sb * sb)
    if s == 0:
        return 0.0 if d == 0 else float("inf")
    return d / s


def hpd_overlap(a, b):
    """Overlap of the two 95 % HPD intervals as a fraction of the narrower one."""
    if any(isnan(v) for v in (a.lo, a.hi, b.lo, b.hi)):
        return NAN
    ov = min(a.hi, b.hi) - max(a.lo, b.lo)
    w = min(a.hi - a.lo, b.hi - b.lo)
    if w <= 0:
        return 1.0 if ov >= 0 else 0.0
    return max(0.0, ov) / w


# --------------------------------------------------------------------------------------
# Trace logs
# --------------------------------------------------------------------------------------

_ALNUM = re.compile(r"[0-9a-zA-Z]")
_DATA = re.compile(r"[-0-9]")


class TraceLog(object):
    """One trace log, post burn-in. Mirrors LogAnalyser.readLogFile."""

    def __init__(self, path, burnin_pct):
        self.path = path
        self.labels = None
        rows = []
        self.malformed = 0
        with open(path, "r", errors="replace") as fh:
            for line in fh:
                if "#" in line:
                    continue
                if self.labels is None:
                    if _ALNUM.search(line):
                        self.labels = line.strip().split("\t")
                    continue
                if not _DATA.match(line):
                    continue          # e.g. a repeated header line
                f = line.strip().split("\t")
                if len(f) != len(self.labels):
                    self.malformed += 1      # truncated last line of a running chain, ...
                    continue
                rows.append(f)
        if self.labels is None:
            raise ValueError("no header line found")
        self.n_data = len(rows)
        self.n_burn = self.n_data * burnin_pct // 100
        rows = rows[self.n_burn:]
        self.n = len(rows)
        self.first_state = self.last_state = self.interval = None
        try:
            if rows:
                self.first_state = int(float(rows[0][0]))
                self.last_state = int(float(rows[-1][0]))
            if len(rows) > 1:
                self.interval = int(float(rows[1][0])) - int(float(rows[0][0]))
        except ValueError:
            pass
        self.columns = OrderedDict()
        self.nominal = []
        for j, lab in enumerate(self.labels[1:], start=1):
            vals = []
            ok = True
            for r in rows:
                t = r[j]
                try:
                    vals.append(float(t))
                except ValueError:
                    tl = t.lower()
                    if tl == "true":
                        vals.append(1.0)
                    elif tl == "false":
                        vals.append(0.0)
                    else:
                        ok = False
                        break
            if ok:
                self.columns[lab] = vals
            else:
                self.nominal.append(lab)


# --------------------------------------------------------------------------------------
# Tree logs
# --------------------------------------------------------------------------------------

_COMMENT = re.compile(r"\[[^\]]*\]")
_TOKEN = re.compile(r"'[^']*'|\"[^\"]*\"|[(),;]|:[^,();]*|[^,();:]+")


def _unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        return s[1:-1]
    return s


class TreeLog(object):
    """Clade frequencies (and optionally root heights) of a NEXUS tree file, post burn-in.

    Streams the file twice: once to count trees, once to parse them."""

    def __init__(self, path, burnin_pct, heights=False, min_freq=0.0):
        self.path = path
        total = 0
        with open(path, "r", errors="replace") as fh:
            for line in fh:
                if line.lstrip()[:5].lower() == "tree ":
                    total += 1
        self.n_total = total
        self.n_burn = total * burnin_pct // 100
        self.n = 0
        self.taxa = set()
        self.heights = [] if heights else None
        counts = Counter()
        translate = {}
        index = {}          # label -> bit position
        names = []
        in_trans = False
        trans_buf = ""
        seen = 0
        with open(path, "r", errors="replace") as fh:
            for line in fh:
                s = line.strip()
                low = s.lower()
                if in_trans or low.startswith("translate"):
                    if not in_trans:
                        s = s[len("translate"):]
                        in_trans = True
                    trans_buf += " " + s
                    if ";" in s:
                        in_trans = False
                        for entry in trans_buf.split(";")[0].split(","):
                            parts = entry.strip().split(None, 1)
                            if len(parts) == 2:
                                translate[parts[0]] = _unquote(parts[1])
                        trans_buf = ""
                    continue
                if low[:5] != "tree ":
                    continue
                seen += 1
                if seen <= self.n_burn:
                    continue
                eq = s.find("=")
                if eq < 0:
                    continue
                newick = _COMMENT.sub("", s[eq + 1:])
                clades, root_h = self._parse(newick, translate, index, names, heights)
                counts.update(clades)
                if heights:
                    self.heights.append(root_h)
                self.n += 1
        self.taxa = set(names)
        # bit masks -> frozensets of taxon names. Clades below min_freq in this file are
        # dropped: a clade can only reach min_freq in the pooled replicates (or in the
        # replicate comparison) if it reaches it in at least one replicate.
        self.clades = {}
        cut = min_freq * self.n
        for mask, c in counts.items():
            if c < cut:
                continue
            members = frozenset(names[i] for i in range(len(names)) if mask >> i & 1)
            self.clades[members] = self.clades.get(members, 0) + c

    @staticmethod
    def _parse(newick, translate, index, names, heights):
        stack = []
        cur = [0, 0.0]          # [taxon mask, max height] of the node being built
        pending = None          # (mask, height) of the last completed child
        plen = 0.0
        after_close = False
        clades = []
        root = None
        for tok in _TOKEN.findall(newick):
            c = tok[0]
            if c == "(":
                stack.append(cur)
                cur = [0, 0.0]
                pending, plen, after_close = None, 0.0, False
            elif c == ":":
                if heights:
                    try:
                        plen = float(tok[1:])
                    except ValueError:
                        plen = 0.0
            elif c == "," or c == ")" or c == ";":
                if pending is not None:
                    cur[0] |= pending[0]
                    h = pending[1] + plen
                    if h > cur[1]:
                        cur[1] = h
                    pending, plen = None, 0.0
                if c == ")":
                    node = (cur[0], cur[1])
                    cur = stack.pop()
                    if stack:
                        clades.append(node[0])
                    else:
                        root = node
                    pending, after_close = node, True
                elif c == ";":
                    break
                else:
                    after_close = False
            else:
                if after_close:
                    continue            # internal node label
                lab = tok.strip()
                if not lab:
                    continue
                lab = translate.get(lab, _unquote(lab))
                i = index.get(lab)
                if i is None:
                    i = index[lab] = len(names)
                    names.append(lab)
                pending, plen = (1 << i, 0.0), 0.0
        if root is None:
            root = pending if pending is not None else (cur[0], cur[1])
        return clades, root[1]


# --------------------------------------------------------------------------------------
# beast.out
# --------------------------------------------------------------------------------------

_EXC = re.compile(r"\b((?:[a-z]\w*\.)+[A-Z]\w*(?:Exception|Error))\b|^\s*(Exception|Error)\b")
_TIME = re.compile(r"Total calculation time:\s*([0-9.eE+-]+)\s*seconds")


class OutInfo(object):
    def __init__(self, path):
        self.path = path
        self.present = os.path.exists(path)
        self.seconds = None
        self.finished = False
        self.errors = []
        self.version = None
        if not self.present:
            return
        with open(path, "r", errors="replace") as fh:
            for line in fh:
                m = _TIME.search(line)
                if m:
                    try:
                        self.seconds = float(m.group(1))
                    except ValueError:
                        pass
                if "End likelihood" in line:
                    self.finished = True
                if self.version is None:
                    mv = re.search(r"BEAST v(\d[\w.\-]*(?: (?:rc|RC|Prerelease|pre)\w*)?)", line)
                    if mv:
                        self.version = mv.group(1).strip()
                if _EXC.search(line) and len(self.errors) < 3:
                    self.errors.append(line.strip()[:200])


# --------------------------------------------------------------------------------------
# Run sets
# --------------------------------------------------------------------------------------

def _key(fname):
    """File-name key used to match logs between replicates/versions (digits ignored,
    so test.1.log in rep1 matches test.2.log in rep2)."""
    return re.sub(r"\d+", "#", fname)


class Side(object):
    """One version: a label plus its replicate directories."""

    def __init__(self, label, dirs):
        self.label = label
        self.rep_dirs = []
        for d in dirs:
            subs = sorted(p for p in glob.glob(os.path.join(d, "rep*")) if os.path.isdir(p))
            self.rep_dirs.extend(subs if subs else [d])
        self.rep_dirs = [d for d in self.rep_dirs if os.path.isdir(d)]
        self.outs = [OutInfo(os.path.join(d, "beast.out")) for d in self.rep_dirs]

    def files(self, ext, pattern=None):
        """OrderedDict key -> list of paths (one per replicate, None if missing)."""
        res = OrderedDict()
        for i, d in enumerate(self.rep_dirs):
            for p in sorted(glob.glob(os.path.join(d, "*" + ext))):
                fn = os.path.basename(p)
                if pattern and not fnmatch.fnmatch(fn, pattern):
                    continue
                res.setdefault(_key(fn), [None] * len(self.rep_dirs))[i] = p
        return res

    def rep_name(self, i):
        return os.path.basename(os.path.normpath(self.rep_dirs[i]))


def pair_files(fa, fb, findings, kind, la, lb):
    pairs = []
    ka, kb = list(fa), list(fb)
    for k in ka:
        if k in fb:
            pairs.append((k, k))
    ra = [k for k in ka if k not in fb]
    rb = [k for k in kb if k not in fa]
    if len(ra) == 1 and len(rb) == 1:
        pairs.append((ra[0], rb[0]))
        findings.append(("NOTE", "%s file names differ: %s `%s` paired with %s `%s`"
                         % (kind, la, ra[0].replace("#", "N"), lb, rb[0].replace("#", "N"))))
    else:
        for k in ra:
            findings.append(("WARN", "%s file `%s` only in %s (use --log/--log-b to select)" % (kind, k.replace("#", "N"), la)))
        for k in rb:
            findings.append(("WARN", "%s file `%s` only in %s (use --log/--log-b to select)" % (kind, k.replace("#", "N"), lb)))
    return pairs


def read_map(path):
    m = OrderedDict()
    if not path:
        return m
    with open(path) as fh:
        for line in fh:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) >= 2 and f[0].strip() and f[1].strip():
                m[f[0].strip()] = f[1].strip()
    return m


# --------------------------------------------------------------------------------------
# Comparison
# --------------------------------------------------------------------------------------

class Row(object):
    def __init__(self, name, col_a, col_b):
        self.name, self.col_a, self.col_b = name, col_a, col_b
        self.a = self.b = None
        self.a_reps, self.b_reps = [], []
        self.z = NAN
        self.overlap = NAN
        self.rep_z_a = self.rep_z_b = NAN
        self.flags = []
        self.section = ""


def max_rep_z(reps):
    zs = [zstat(x, y) for x, y in itertools.combinations(reps, 2)]
    zs = [z for z in zs if not isnan(z)]
    return max(zs) if zs else NAN


def compare_columns(name, col_a, col_b, vals_a, vals_b, opts):
    """vals_a / vals_b: list of per-replicate value lists."""
    r = Row(name, col_a, col_b)
    r.a_reps = [summarise(v) for v in vals_a]
    r.b_reps = [summarise(v) for v in vals_b]
    r.a = combine(vals_a, r.a_reps)
    r.b = combine(vals_b, r.b_reps)
    r.z = zstat(r.a, r.b)
    r.overlap = hpd_overlap(r.a, r.b)
    r.rep_z_a = max_rep_z(r.a_reps)
    r.rep_z_b = max_rep_z(r.b_reps)
    if r.a.constant and r.b.constant:
        if r.a.mean != r.b.mean:
            r.flags.append("const-diff")
        return r
    if not isnan(r.z) and r.z >= opts.z_flag:
        r.flags.append("z")
    if not isnan(r.overlap) and r.overlap < opts.hpd_overlap:
        r.flags.append("hpd")
    low = [s.ess for s in r.a_reps + r.b_reps if not s.constant]
    if any(isnan(e) or e < opts.min_ess for e in low):
        r.flags.append("ess")
    return r


class Result(object):
    def __init__(self, name):
        self.name = name
        self.sections = []      # (title, rows, const_rows, only_a, only_b, log info)
        self.clades = []        # (title, clade rows, n_a, n_b, rep_dp_a, rep_dp_b, height_row)
        self.findings = []
        self.verdict = ""
        self.min_ess = NAN
        self.max_z = NAN
        self.max_dp = NAN
        self.n_flagged = 0


def run_comparison(name, side_a, side_b, opts, mapping):
    res = Result(name)
    F = res.findings
    la, lb = side_a.label, side_b.label
    for side in (side_a, side_b):
        if not side.rep_dirs:
            F.append(("FAIL", "no replicate directories for %s" % side.label))
        elif len(side.rep_dirs) < 2:
            F.append(("WARN", "%s has only %d replicate (README asks for >= 2)" % (side.label, len(side.rep_dirs))))
        for i, o in enumerate(side.outs):
            rn = side.rep_name(i)
            if not o.present:
                F.append(("NOTE", "%s %s: no beast.out" % (side.label, rn)))
                continue
            if o.errors:
                F.append(("FAIL", "%s %s: beast.out reports an error: `%s`" % (side.label, rn, o.errors[0])))
            if not o.finished:
                F.append(("FAIL", "%s %s: beast.out has no 'End likelihood' line (run did not finish?)" % (side.label, rn)))
        vers = sorted(set(o.version for o in side.outs if o.version))
        if len(vers) > 1:
            F.append(("WARN", "%s replicates were run with different BEAST versions: %s" % (side.label, ", ".join(vers))))
    if not side_a.rep_dirs or not side_b.rep_dirs:
        res.verdict = "no comparison"
        return res

    # ---- trace logs
    fa = side_a.files(".log", opts.log)
    fb = side_b.files(".log", opts.log_b or opts.log)
    pairs = pair_files(fa, fb, F, "Trace log", la, lb)
    if not pairs:
        F.append(("FAIL", "no trace logs to compare"))
    used_map = set()
    for ka, kb in pairs:
        logs = {}
        info = []
        for side, files, k in ((side_a, fa, ka), (side_b, fb, kb)):
            lst = []
            for i, p in enumerate(files[k]):
                if p is None:
                    F.append(("WARN", "%s %s: no `%s`" % (side.label, side.rep_name(i), k.replace("#", "N"))))
                    continue
                try:
                    t = TraceLog(p, opts.burnin)
                except (OSError, ValueError) as e:
                    F.append(("FAIL", "%s: cannot read %s: %s" % (side.label, p, e)))
                    continue
                if t.malformed:
                    F.append(("NOTE", "%s %s: %d malformed/truncated line(s) in %s skipped"
                              % (side.label, side.rep_name(i), t.malformed, os.path.basename(p))))
                if t.n < 2:
                    F.append(("FAIL", "%s %s: %s has fewer than 2 samples after burn-in" % (side.label, side.rep_name(i), os.path.basename(p))))
                    continue
                lst.append(t)
                info.append((side.label, side.rep_name(i), os.path.relpath(p, opts.relto), t))
            logs[side.label] = lst
        ta, tb = logs[la], logs[lb]
        if not ta or not tb:
            continue
        cols_a = [c for c in ta[0].columns if all(c in t.columns for t in ta)]
        cols_b = [c for c in tb[0].columns if all(c in t.columns for t in tb)]
        set_b = set(cols_b)
        matched = []
        taken_b = set()
        for ca, cb in mapping.items():
            if ca in cols_a and cb in set_b:
                matched.append((ca, cb))
                taken_b.add(cb)
                used_map.add(ca)
        mapped_a = set(c for c, _ in matched)
        for c in cols_a:
            if c not in mapped_a and c in set_b and c not in taken_b:
                matched.append((c, c))
                taken_b.add(c)
        order = {c: i for i, c in enumerate(cols_a)}
        matched.sort(key=lambda p: order[p[0]])
        only_a = [c for c in cols_a if c not in set(m[0] for m in matched)]
        only_b = [c for c in cols_b if c not in taken_b]
        title = ka.replace("#", "N") if ka == kb else "%s / %s" % (ka.replace("#", "N"), kb.replace("#", "N"))
        rows, consts = [], []
        for ca, cb in matched:
            nm = ca if ca == cb else "%s → %s" % (ca, cb)
            r = compare_columns(nm, ca, cb, [t.columns[ca] for t in ta], [t.columns[cb] for t in tb], opts)
            r.section = title
            (consts if (r.a.constant and r.b.constant) else rows).append(r)
            if ca != cb:
                F.append(("NOTE", "column renamed (mapping): %s `%s` = %s `%s`" % (la, ca, lb, cb)))
            if "const-diff" in r.flags:
                F.append(("FAIL", "`%s` is constant in both versions but with different values (%s vs %s)"
                          % (nm, fmt(r.a.mean), fmt(r.b.mean))))
        for side_label, only, other in ((la, only_a, only_b), (lb, only_b, only_a)):
            for c in only:
                hint = difflib.get_close_matches(c, other, n=1, cutoff=0.5)
                F.append(("WARN", "column `%s` only in %s%s; add a line to the --map file if it is a renaming"
                          % (c, side_label, (" (maybe `%s`?)" % hint[0]) if hint else "")))
        for t in ta + tb:
            for c in t.nominal:
                F.append(("NOTE", "non-numeric column `%s` in %s ignored" % (c, os.path.basename(t.path))))
                break
        res.sections.append((title, rows, consts, only_a, only_b, info))
    for ca in mapping:
        if ca not in used_map and pairs:
            F.append(("NOTE", "map entry `%s` -> `%s` not used (column not present)" % (ca, mapping[ca])))

    # ---- trees
    if not opts.no_trees:
        ta_files = side_a.files(".trees", opts.trees)
        tb_files = side_b.files(".trees", opts.trees_b or opts.trees)
        if ta_files and tb_files:
            for ka, kb in pair_files(ta_files, tb_files, F, "Tree", la, lb):
                trees = {}
                for side, files, k in ((side_a, ta_files, ka), (side_b, tb_files, kb)):
                    lst = []
                    for i, p in enumerate(files[k]):
                        if p is None:
                            continue
                        try:
                            lst.append(TreeLog(p, opts.burnin, heights=opts.tree_height, min_freq=opts.clade_min))
                        except (OSError, ValueError, IndexError) as e:
                            F.append(("FAIL", "%s: cannot parse %s: %s" % (side.label, p, e)))
                    trees[side.label] = lst
                A, B = trees[la], trees[lb]
                if not A or not B or not all(t.n for t in A + B):
                    F.append(("WARN", "tree file `%s`: no trees after burn-in in one version" % ka.replace("#", "N")))
                    continue
                title = ka.replace("#", "N") if ka == kb else "%s / %s" % (ka.replace("#", "N"), kb.replace("#", "N"))
                taxa_a = set().union(*[t.taxa for t in A])
                taxa_b = set().union(*[t.taxa for t in B])
                if taxa_a != taxa_b:
                    F.append(("FAIL", "trees `%s`: taxon sets differ (only in %s: %s; only in %s: %s)"
                              % (title, la, sorted(taxa_a - taxa_b)[:5], lb, sorted(taxa_b - taxa_a)[:5])))

                def freqs(lst):
                    tot = Counter()
                    n = 0
                    for t in lst:
                        tot.update(t.clades)
                        n += t.n
                    return {c: v / float(n) for c, v in tot.items()}, n

                pa, na = freqs(A)
                pb, nb = freqs(B)

                def rep_dp(lst):
                    best = NAN
                    for x, y in itertools.combinations(lst, 2):
                        px = {c: v / float(x.n) for c, v in x.clades.items()}
                        py = {c: v / float(y.n) for c, v in y.clades.items()}
                        for c in set(px) | set(py):
                            if max(px.get(c, 0), py.get(c, 0)) >= opts.clade_min:
                                d = abs(px.get(c, 0) - py.get(c, 0))
                                if isnan(best) or d > best:
                                    best = d
                    return best

                crow = []
                for c in set(pa) | set(pb):
                    a, b = pa.get(c, 0.0), pb.get(c, 0.0)
                    if max(a, b) >= opts.clade_min:
                        crow.append((c, a, b, abs(a - b), abs(a - b) > opts.clade_diff))
                crow.sort(key=lambda r: (-r[3], -max(r[1], r[2]), len(r[0]), sorted(r[0])))
                hrow = None
                if opts.tree_height:
                    hrow = compare_columns("tree height (from %s)" % title, "", "",
                                           [t.heights for t in A], [t.heights for t in B], opts)
                res.clades.append((title, crow, na, nb, rep_dp(A), rep_dp(B), hrow))
                if not isnan(rep_dp(A)) and rep_dp(A) > opts.clade_diff:
                    F.append(("WARN", "%s replicates disagree on a clade (|Δp| = %.3f): tree sampling not converged?" % (la, rep_dp(A))))
                if not isnan(rep_dp(B)) and rep_dp(B) > opts.clade_diff:
                    F.append(("WARN", "%s replicates disagree on a clade (|Δp| = %.3f): tree sampling not converged?" % (lb, rep_dp(B))))
        elif ta_files or tb_files:
            F.append(("NOTE", "tree files present in only one version; clades not compared"))

    # ---- verdict
    allrows = [r for s in res.sections for r in s[1]]
    allrows += [c[6] for c in res.clades if c[6] is not None]
    esses = [s.ess for r in allrows for s in r.a_reps + r.b_reps if not s.constant]
    if any(isnan(e) for e in esses):
        res.min_ess = NAN          # a non-constant column without a usable ESS
    else:
        res.min_ess = min(esses) if esses else NAN
    zs = [r.z for r in allrows if not isnan(r.z)]
    res.max_z = max(zs) if zs else NAN
    dps = [cr[3] for c in res.clades for cr in c[1]]
    res.max_dp = max(dps) if dps else NAN

    flagged = []
    fail = False
    for r in allrows:
        if "z" in r.flags or "hpd" in r.flags:
            flagged.append(r.name)
            if r.z >= opts.z_fail:
                fail = True
        if "const-diff" in r.flags:
            fail = True
        if "z" in r.flags:
            F.append(("FLAG", "`%s`: z = %.2f (%s mean %s, %s mean %s)" % (r.name, r.z, la, fmt(r.a.mean), lb, fmt(r.b.mean))))
        if "z" in r.flags and re.search(r"posterior|prior|likelihood", r.name, re.I) \
                and r.a.sd > 0 and r.b.sd > 0 and 0.8 < r.a.sd / r.b.sd < 1.25:
            F.append(("NOTE", "`%s` is shifted by %s with about the same sd: if all model parameters match, this is "
                      "probably a constant offset in the log density (e.g. a prior's normalising constant or bounds), "
                      "not a different posterior. Check the XMLs before raising an issue."
                      % (r.name, fmt(r.b.mean - r.a.mean))))
        if "hpd" in r.flags:
            F.append(("FLAG", "`%s`: 95%% HPD intervals overlap only %.0f%% of the narrower one" % (r.name, 100 * r.overlap)))
        for lab, z in ((la, r.rep_z_a), (lb, r.rep_z_b)):
            if not isnan(z) and z >= opts.z_flag:
                F.append(("WARN", "`%s`: %s replicates disagree with each other (z = %.2f)" % (r.name, lab, z)))
    for title, crow, na, nb, _, _, _ in res.clades:
        for c, a, b, d, fl in crow:
            if fl:
                flagged.append("clade " + clade_str(c))
                if d > opts.clade_fail:
                    fail = True
                F.append(("FLAG", "clade %s: p = %.3f (%s) vs %.3f (%s), |Δp| = %.3f" % (clade_str(c), a, la, b, lb, d)))
    low = sorted(set((r.name, lab, s_i) for r in allrows
                     for lab, reps in ((la, r.a_reps), (lb, r.b_reps))
                     for s_i, s in enumerate(reps) if not s.constant and (isnan(s.ess) or s.ess < opts.min_ess)))
    if low:
        names = OrderedDict()
        for nm, lab, _ in low:
            names.setdefault(nm, set()).add(lab)
        F.append(("WARN", "ESS < %g in at least one replicate for %d column(s): %s. README: rerun longer before comparing"
                  % (opts.min_ess, len(names), ", ".join("`%s` (%s)" % (k, "/".join(sorted(v))) for k, v in names.items()))))
    res.n_flagged = len(flagged)
    if not allrows and not res.clades:
        res.verdict = "no comparison"
    elif fail or len(flagged) > opts.max_borderline:
        res.verdict = "not matched"
    elif flagged:
        res.verdict = "borderline"
    else:
        res.verdict = "matched"
    if res.verdict != "no comparison":
        if low:
            res.verdict += " (ESS < %g)" % opts.min_ess
        if any(f[0] == "FAIL" for f in F):
            res.verdict += " (run problems)"
    return res


# --------------------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------------------

def fmt(x):
    if x is None or isnan(x):
        return "–"
    if math.isinf(x):
        return "inf"
    a = abs(x)
    if a == 0:
        return "0"
    if a >= 1e5 or a < 1e-3:
        return "%.3e" % x
    if a >= 100:
        return "%.2f" % x
    return "%.4g" % x


def fmt_ess(x):
    return "–" if isnan(x) else "%.0f" % x


def fmt_hpd(s):
    return "[%s, %s]" % (fmt(s.lo), fmt(s.hi))


def clade_str(c, maxn=6):
    names = sorted(c)
    if len(names) > maxn:
        return "{" + ", ".join(names[:maxn]) + ", … (%d taxa)}" % len(names)
    return "{" + ", ".join(names) + "}"


def ess_cell(st, reps, minimum):
    m = min((s.ess for s in reps), default=NAN)
    mark = " ⚠" if (not st.constant and (isnan(m) or m < minimum)) else ""
    return "%s (%s)%s" % (fmt_ess(st.ess), fmt_ess(m), mark)


def flag_cell(r):
    f = []
    if "z" in r.flags:
        f.append("**z**")
    if "hpd" in r.flags:
        f.append("**HPD**")
    if "const-diff" in r.flags:
        f.append("**const**")
    if "ess" in r.flags:
        f.append("low ESS")
    return ", ".join(f) if f else "ok"


def render(res, side_a, side_b, opts):
    la, lb = side_a.label, side_b.label
    o = []
    w = o.append
    w("# Posterior comparison: %s" % res.name)
    w("")
    w("**Verdict: %s**" % res.verdict)
    w("")
    w("- %s: %s" % (la, ", ".join("`%s`" % os.path.relpath(d, opts.relto) for d in side_a.rep_dirs) or "–"))
    w("- %s: %s" % (lb, ", ".join("`%s`" % os.path.relpath(d, opts.relto) for d in side_b.rep_dirs) or "–"))
    w("- burn-in %d%% per replicate; replicates combined by concatenation, combined ESS = sum of replicate ESS" % opts.burnin)
    w("- thresholds: flag z ≥ %g (fail ≥ %g), HPD overlap < %d%%, ESS < %g, clades p ≥ %g with |Δp| > %g (fail > %g); "
      "borderline = at most %d flagged item(s), none failing"
      % (opts.z_flag, opts.z_fail, round(100 * opts.hpd_overlap), opts.min_ess, opts.clade_min, opts.clade_diff,
         opts.clade_fail, opts.max_borderline))
    w("- min ESS (any replicate): %s; max z: %s; max clade |Δp|: %s"
      % (fmt_ess(res.min_ess), fmt(res.max_z), "–" if isnan(res.max_dp) else "%.3f" % res.max_dp))
    w("")
    w("## Findings")
    w("")
    if res.findings:
        order = {"FAIL": 0, "FLAG": 1, "WARN": 2, "NOTE": 3}
        for sev, txt in sorted(res.findings, key=lambda f: order.get(f[0], 9)):
            w("- **%s** %s" % (sev, txt))
    else:
        w("- none")
    w("")

    # runs
    w("## Runs")
    w("")
    w("| Version | Rep | File | Samples (after burn-in) | Interval | BEAST | Finished | Run time | Error |")
    w("|---|---|---|---:|---:|---|---|---:|---|")
    for title, rows, consts, only_a, only_b, info in res.sections:
        for lab, rep, path, t in info:
            side = side_a if lab == la else side_b
            out = None
            for i, d in enumerate(side.rep_dirs):
                if side.rep_name(i) == rep:
                    out = side.outs[i]
            fin = "–" if out is None or not out.present else ("yes" if out.finished else "**no**")
            rt = "–" if out is None or out.seconds is None else hms(out.seconds)
            err = "" if out is None or not out.errors else "`%s`" % out.errors[0][:80]
            ver = "–" if out is None or not out.version else out.version
            w("| %s | %s | `%s` | %d (%d) | %s | %s | %s | %s | %s |"
              % (lab, rep, path, t.n_data, t.n, t.interval if t.interval else "–", ver, fin, rt, err))
    w("")

    for title, rows, consts, only_a, only_b, info in res.sections:
        w("## Parameters: `%s`" % title)
        w("")
        if not rows:
            w("No non-constant columns in common.")
            w("")
        if consts:
            w("Constant columns (skipped): " + ", ".join("`%s` = %s%s" % (r.name, fmt(r.a.mean),
                                                                          "" if r.a.mean == r.b.mean else " vs %s" % fmt(r.b.mean))
                                                        for r in consts))
            w("")
        if only_a or only_b:
            w("Not compared: only in %s: %s; only in %s: %s"
              % (la, ", ".join("`%s`" % c for c in only_a) or "–", lb, ", ".join("`%s`" % c for c in only_b) or "–"))
            w("")
        if not rows:
            continue
        w("ESS column: combined ESS (minimum over replicates).")
        w("")
        w("| Parameter | %s mean | %s 95%% HPD | %s ESS | %s mean | %s 95%% HPD | %s ESS | z | HPD overlap | Flag |"
          % (la, la, la, lb, lb, lb))
        w("|---|---:|---|---:|---:|---|---:|---:|---:|---|")
        for r in rows:
            w("| `%s` | %s | %s | %s | %s | %s | %s | %s | %s | %s |"
              % (r.name, fmt(r.a.mean), fmt_hpd(r.a), ess_cell(r.a, r.a_reps, opts.min_ess),
                 fmt(r.b.mean), fmt_hpd(r.b), ess_cell(r.b, r.b_reps, opts.min_ess),
                 "–" if isnan(r.z) else "%.2f" % r.z,
                 "–" if isnan(r.overlap) else "%.0f%%" % (100 * r.overlap), flag_cell(r)))
        w("")
        w("### Replicate agreement (baseline noise): `%s`" % title)
        w("")
        w("Largest z between two replicates of the same version (same formula as above, per-replicate se).")
        w("")
        w("| Parameter | %s rep means | %s max z | %s rep means | %s max z |" % (la, la, lb, lb))
        w("|---|---|---:|---|---:|")
        for r in rows:
            w("| `%s` | %s | %s | %s | %s |"
              % (r.name, ", ".join(fmt(s.mean) for s in r.a_reps), "–" if isnan(r.rep_z_a) else "%.2f" % r.rep_z_a,
                 ", ".join(fmt(s.mean) for s in r.b_reps), "–" if isnan(r.rep_z_b) else "%.2f" % r.rep_z_b))
        w("")

    for title, crow, na, nb, dpa, dpb, hrow in res.clades:
        w("## Trees: `%s`" % title)
        w("")
        w("%d trees (%s) and %d trees (%s) after burn-in. Clades with p ≥ %g in either version; "
          "flag |Δp| > %g. Largest |Δp| between replicates: %s %s, %s %s."
          % (na, la, nb, lb, opts.clade_min, opts.clade_diff,
             la, "–" if isnan(dpa) else "%.3f" % dpa, lb, "–" if isnan(dpb) else "%.3f" % dpb))
        w("")
        w("| Clade | Size | p %s | p %s | abs Δp | Flag |" % (la, lb))
        w("|---|---:|---:|---:|---:|---|")
        shown = [c for c in crow if c[4]] + [c for c in crow if not c[4]][:max(0, opts.max_clades - sum(1 for c in crow if c[4]))]
        for c, a, b, d, fl in shown:
            w("| %s | %d | %.3f | %.3f | %.3f | %s |" % (clade_str(c), len(c), a, b, d, "**Δp**" if fl else "ok"))
        if len(shown) < len(crow):
            w("")
            w("(%d more clades with |Δp| ≤ %g not shown; see the .clades.tsv file)" % (len(crow) - len(shown), opts.clade_diff))
        w("")
        if hrow is not None:
            r = hrow
            w("Tree height from the tree file: %s mean %s %s ESS %s; %s mean %s %s ESS %s; z = %s (%s)"
              % (la, fmt(r.a.mean), fmt_hpd(r.a), ess_cell(r.a, r.a_reps, opts.min_ess),
                 lb, fmt(r.b.mean), fmt_hpd(r.b), ess_cell(r.b, r.b_reps, opts.min_ess),
                 "–" if isnan(r.z) else "%.2f" % r.z, flag_cell(r)))
            w("")

    # speed
    w("## Speed")
    w("")
    sp = speed(res, side_a, side_b)
    if sp:
        w("| Version | Total run time | Combined ESS of `%s` | ESS/hour | Min ESS/hour (any column) |" % sp[0][1])
        w("|---|---:|---:|---:|---:|")
        for lab, col, secs, e, eph, mineph, mincol in sp:
            w("| %s | %s | %s | %s | %s (`%s`) |" % (lab, hms(secs), fmt_ess(e), fmt_ess(eph), fmt_ess(mineph), mincol))
        if len(sp) == 2 and sp[0][2] and sp[1][2]:
            w("")
            w("Run-time ratio %s / %s: %.2f" % (lb, la, sp[1][2] / sp[0][2]))
    else:
        w("Run time not available (no `Total calculation time` in beast.out).")
    w("")
    return "\n".join(o)


def hms(s):
    if s is None:
        return "–"
    s = int(round(s))
    if s < 60:
        return "%ds" % s
    if s < 3600:
        return "%dm%02ds" % (s // 60, s % 60)
    return "%dh%02dm" % (s // 3600, (s % 3600) // 60)


def side_seconds(side):
    secs = [o.seconds for o in side.outs]
    if not secs or any(s is None for s in secs):
        return None
    return sum(secs)


def speed(res, side_a, side_b):
    rows = [r for s in res.sections for r in s[1]]
    if not rows:
        return []
    ref = None
    for r in rows:
        if r.col_a.lower() in ("posterior",):
            ref = r
    ref = ref or rows[0]
    out = []
    for side, get in ((side_a, lambda r: r.a), (side_b, lambda r: r.b)):
        secs = side_seconds(side)
        if not secs:
            continue
        h = secs / 3600.0
        e = get(ref).ess
        cand = [(get(r).ess / h, r.name) for r in rows if not isnan(get(r).ess)]
        mn = min(cand) if cand else (NAN, "–")
        out.append((side.label, ref.name, secs, e, e / h if not isnan(e) else NAN, mn[0], mn[1]))
    return out


def write_tsv(path, res, side_a, side_b):
    la, lb = side_a.label, side_b.label
    ha, hb = side_seconds(side_a), side_seconds(side_b)
    hdr = ["log", "parameter", "col_" + la, "col_" + lb]
    for lab in (la, lb):
        hdr += [lab + x for x in ("_mean", "_sd", "_hpd_lo", "_hpd_hi", "_ess", "_min_rep_ess", "_ess_per_hour", "_rep_max_z")]
    hdr += ["z", "hpd_overlap", "flags"]
    g = lambda x: "" if x is None or isnan(x) else "%.10g" % x
    with open(path, "w") as fh:
        fh.write("\t".join(hdr) + "\n")
        for title, rows, consts, _, _, _ in res.sections:
            for r in rows + consts:
                f = [title, r.name, r.col_a, r.col_b]
                for st, reps, secs, rz in ((r.a, r.a_reps, ha, r.rep_z_a), (r.b, r.b_reps, hb, r.rep_z_b)):
                    m = min((s.ess for s in reps), default=NAN)
                    f += [g(st.mean), g(st.sd), g(st.lo), g(st.hi), g(st.ess), g(m),
                          g(st.ess / (secs / 3600.0)) if secs and not isnan(st.ess) else "", g(rz)]
                flags = list(r.flags) + (["constant"] if r in consts else [])
                f += [g(r.z), g(r.overlap), ",".join(flags)]
                fh.write("\t".join(f) + "\n")
    if res.clades:
        cpath = path[:-4] + ".clades.tsv"
        with open(cpath, "w") as fh:
            fh.write("\t".join(["trees", "clade", "size", "p_" + la, "p_" + lb, "abs_dp", "flag"]) + "\n")
            for title, crow, _, _, _, _, _ in res.clades:
                for c, a, b, d, fl in crow:
                    fh.write("%s\t%s\t%d\t%.6f\t%.6f\t%.6f\t%s\n" % (title, " ".join(sorted(c)), len(c), a, b, d, "dp" if fl else ""))


def plots(res, side_a, side_b, outdir, name, logsets):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        sys.stderr.write("--plots: matplotlib is not installed (pip3 install matplotlib); skipping plots\n")
        return
    d = os.path.join(outdir, name + "-plots")
    os.makedirs(d, exist_ok=True)
    n = 0
    for title, rows, _, _, _, _ in res.sections:
        ta, tb = logsets.get(title, (None, None))
        if not ta:
            continue
        for r in rows:
            va = [v for t in ta for v in t.columns[r.col_a]]
            vb = [v for t in tb for v in t.columns[r.col_b]]
            fig, ax = plt.subplots(figsize=(5, 3.2))
            lo, hi = min(min(va), min(vb)), max(max(va), max(vb))
            bins = 50 if hi > lo else 1
            ax.hist(va, bins=bins, range=(lo, hi) if hi > lo else None, density=True, histtype="step", label=side_a.label)
            ax.hist(vb, bins=bins, range=(lo, hi) if hi > lo else None, density=True, histtype="step", label=side_b.label)
            ax.set_title("%s (z = %s)" % (r.name, fmt(r.z)), fontsize=9)
            ax.legend(fontsize=8)
            fig.tight_layout()
            fig.savefig(os.path.join(d, re.sub(r"[^\w.-]+", "_", r.name) + ".png"), dpi=100)
            plt.close(fig)
            n += 1
    sys.stderr.write("wrote %d plots to %s\n" % (n, d))


# --------------------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------------------

def compare_one(name, side_a, side_b, opts, mapfile):
    mapping = read_map(mapfile)
    res = run_comparison(name, side_a, side_b, opts, mapping)
    if mapfile:
        res.findings.append(("NOTE", "column map used: `%s` (%d entries)" % (os.path.relpath(mapfile, opts.relto), len(mapping))))
    text = render(res, side_a, side_b, opts)
    if not opts.no_write:
        os.makedirs(opts.out, exist_ok=True)
        safe = re.sub(r"[^\w.+-]+", "_", name)
        with open(os.path.join(opts.out, safe + ".md"), "w") as fh:
            fh.write(text + "\n")
        write_tsv(os.path.join(opts.out, safe + ".tsv"), res, side_a, side_b)
    if opts.plots:
        logsets = {}
        for title, rows, consts, oa, ob, info in res.sections:
            logsets[title] = ([t for lab, _, _, t in info if lab == side_a.label],
                              [t for lab, _, _, t in info if lab == side_b.label])
        plots(res, side_a, side_b, opts.out, re.sub(r"[^\w.+-]+", "_", name), logsets)
    return res, text


def default_map(opts, name):
    if opts.map:
        return opts.map
    p = os.path.join(opts.map_dir, name + ".tsv")
    return p if os.path.exists(p) else None


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(
        description="Compare BEAST posteriors (BEAST 2.7.9 vs BEAST 3, or any two sets of runs).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("\n\n", 1)[1])
    ap.add_argument("name", nargs="?", help="combination/example name, e.g. beauti-C07 or testHKY")
    ap.add_argument("--all", action="store_true", help="batch mode: every <name> with logs in both versions")
    ap.add_argument("--root", default=os.path.dirname(here), help="repository root (default: parent of scripts/)")
    ap.add_argument("--a", nargs="+", metavar="DIR", help="run directories of set A (rep dirs, or dirs containing rep*/)")
    ap.add_argument("--b", nargs="+", metavar="DIR", help="run directories of set B")
    ap.add_argument("--label-a", default=None, help="label for set A (default beast2, or A with --a/--b)")
    ap.add_argument("--label-b", default=None, help="label for set B (default beast3, or B with --a/--b)")
    ap.add_argument("--name", dest="outname", help="report name when using --a/--b")
    ap.add_argument("-b", "--burnin", type=int, default=10, help="burn-in percentage per replicate (default 10)")
    ap.add_argument("--map", help="TSV file: <A column><TAB><B column> per line (default: reports/maps/<name>.tsv if present)")
    ap.add_argument("--map-dir", default=None, help="directory with <name>.tsv column maps (default <root>/reports/maps)")
    ap.add_argument("--log", help="glob selecting trace logs in each rep dir, e.g. 'beauti-C07.log'")
    ap.add_argument("--log-b", help="glob for set B if it differs from --log")
    ap.add_argument("--trees", help="glob selecting tree files")
    ap.add_argument("--trees-b", help="glob for set B tree files if it differs from --trees")
    ap.add_argument("--no-trees", action="store_true", help="skip the tree comparison")
    ap.add_argument("--tree-height", action="store_true", help="also compare root height computed from the tree files")
    ap.add_argument("--z-flag", type=float, default=3.0, help="flag a parameter with z >= this (default 3)")
    ap.add_argument("--z-fail", type=float, default=4.0, help="z >= this makes the result 'not matched' (default 4)")
    ap.add_argument("--max-borderline", type=int, default=1, help="max flagged items for 'borderline' (default 1)")
    ap.add_argument("--hpd-overlap", type=float, default=0.5,
                    help="flag when HPD overlap < this fraction of the narrower interval (default 0.5)")
    ap.add_argument("--min-ess", type=float, default=200, help="ESS threshold per replicate (default 200)")
    ap.add_argument("--clade-min", type=float, default=0.05, help="consider clades with p >= this in either set (default 0.05)")
    ap.add_argument("--clade-diff", type=float, default=0.1, help="flag clades with |dp| > this (default 0.1)")
    ap.add_argument("--clade-fail", type=float, default=0.2, help="|dp| > this makes the result 'not matched' (default 0.2)")
    ap.add_argument("--max-clades", type=int, default=30, help="clade rows shown in the report (default 30)")
    ap.add_argument("--out", help="output directory (default <root>/reports/summary)")
    ap.add_argument("--no-write", action="store_true", help="print only, do not write report files")
    ap.add_argument("--plots", action="store_true", help="save marginal density overlays (needs matplotlib)")
    ap.add_argument("-q", "--quiet", action="store_true", help="do not print the report to stdout")
    opts = ap.parse_args(argv)

    opts.root = os.path.abspath(opts.root)
    opts.out = os.path.abspath(opts.out or os.path.join(opts.root, "reports", "summary"))
    opts.map_dir = opts.map_dir or os.path.join(opts.root, "reports", "maps")
    opts.relto = opts.root
    la = opts.label_a or "beast2"
    lb = opts.label_b or "beast3"

    if opts.a or opts.b:
        if not (opts.a and opts.b):
            ap.error("--a and --b must be given together")
        name = opts.outname or opts.name or "custom"
        res, text = compare_one(name, Side(la if opts.label_a else "A", opts.a), Side(lb if opts.label_b else "B", opts.b),
                                opts, opts.map)
        if not opts.quiet:
            print(text)
        return 0

    log_a = os.path.join(opts.root, "beast2", "log")
    log_b = os.path.join(opts.root, "beast3", "log")
    if opts.all:
        names = sorted(set(os.listdir(log_a) if os.path.isdir(log_a) else []) &
                       set(os.listdir(log_b) if os.path.isdir(log_b) else []))
        names = [n for n in names if os.path.isdir(os.path.join(log_a, n)) and os.path.isdir(os.path.join(log_b, n))]
        if not names:
            ap.error("no <name> has logs in both %s and %s" % (log_a, log_b))
        lines = ["# Batch comparison (%s vs %s, burn-in %d%%)" % (la, lb, opts.burnin), "",
                 "| Name | Reps (%s/%s) | Min ESS | Max z | Max clade Δp | Flagged | Verdict |" % (la, lb),
                 "|---|---|---:|---:|---:|---:|---|"]
        for n in names:
            sa, sb = Side(la, [os.path.join(log_a, n)]), Side(lb, [os.path.join(log_b, n)])
            try:
                res, _ = compare_one(n, sa, sb, opts, default_map(opts, n))
                lines.append("| %s | %d/%d | %s | %s | %s | %d | %s |"
                             % (n, len(sa.rep_dirs), len(sb.rep_dirs), fmt_ess(res.min_ess), fmt(res.max_z),
                                "–" if isnan(res.max_dp) else "%.3f" % res.max_dp, res.n_flagged, res.verdict))
            except Exception as e:  # keep going in batch mode
                lines.append("| %s | | | | | | error: %s |" % (n, str(e)[:80]))
        only = sorted(set(os.listdir(log_a) if os.path.isdir(log_a) else []) ^ set(os.listdir(log_b) if os.path.isdir(log_b) else []))
        only = [x for x in only if not x.startswith(".")]
        if only:
            lines += ["", "Only in one version (not compared): " + ", ".join(only)]
        text = "\n".join(lines)
        print(text)
        if not opts.no_write:
            os.makedirs(opts.out, exist_ok=True)
            with open(os.path.join(opts.out, "batch-summary.md"), "w") as fh:
                fh.write(text + "\n")
        return 0

    if not opts.name:
        ap.error("give a <name>, --all, or --a/--b")
    res, text = compare_one(opts.name, Side(la, [os.path.join(log_a, opts.name)]),
                            Side(lb, [os.path.join(log_b, opts.name)]), opts, default_map(opts, opts.name))
    if not opts.quiet:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
