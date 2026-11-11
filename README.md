# beast3-test

Validation of the BEAST 2 example XMLs against their BEAST 3 conversions.

The goal is to show that every example XML shipped with BEAST 2 (v2.7.8) either
has an equivalent BEAST 3 XML that samples the **same posterior**, or is
documented as not yet converted / not applicable.

- BEAST 2 examples (source of truth):
  <https://github.com/CompEvol/beast2/tree/master/examples> — top-level files only, **sub-folders are excluded**.
- BEAST 3 converted examples:
  <https://github.com/CompEvol/beast3/tree/master/beast-base/src/test/resources/beast.base/examples> — top-level `*.xml` / `*.json`.
  (`examples/legacy/` in beast3 holds unconverted BEAST 2 copies)

### Packages

Whether the main packages (ORC, SA, MM, SSM, bModelTest, StarBeast3) still work with the current
BEAST 3 is a separate check, run with one script: see [packages/README.md](packages/README.md).
The latest result is [reports/packages-check.md](reports/packages-check.md).

### Github issue to track

Please use https://github.com/CompEvol/beast3/issues/183 as a reference to track pull requests or changes to [beast3 repo](https://github.com/CompEvol/beast3) during testing. 
However, bug fixes will require a separate issue.

### What to test

Test the `*.xml` / `*.json` files sitting **directly** in each `examples/` folder.
Nothing in a sub-folder is tested, in either repository.

| Repository | Location | What it is | To test? |
|------------|----------|------------|----------|
| beast2 `examples/` | top-level `*.xml` / `*.json` | the BEAST 2 examples (see [Example inventory](#example-inventory)) | ✅ **Yes** — run with BEAST 2.7.9 as the reference |
| beast2 `examples/` | `testStarBeast.xml`, `testStarBeastFBD.xml` | *BEAST 1 examples | ❌ No — *BEAST 1 code was not migrated to BEAST 3 |
| beast2 `examples/` | `parameterised/`, `starbeastinit/`, `beast2vs1/` | extra XMLs: a parameterised RSV2 analysis, *BEAST starting-tree tests, long-run BEAST 2 vs BEAST 1 comparisons | ❌ No — not part of the examples |
| beast2 `examples/` | `benchmark/`, `testDirichlet/` | benchmark and Dirichlet test XMLs | ❌ No — not part of the examples |
| beast2 `examples/` | `fasta/`, `nexus/` | alignment files only | ❌ No — data, not tests |
| beast3 `examples/` | top-level `*.xml` / `*.json` | BEAST 3 conversions of the BEAST 2 examples | ✅ **Yes** — run with BEAST 3 and compare against the BEAST 2 run of the same name |
| beast3 `examples/` | `beast2vs1/` | long-run BEAST 2 vs BEAST 1 comparisons, not for release | ❌ No — not part of the examples |
| beast3 `examples/` | `fasta/`, `nexus/` | alignment files only | ❌ No — data, not tests |

> **Note:** beast3 `examples/legacy/` holds copies of the BEAST 2 XMLs that have **not been
> converted** to BEAST 3. They are **not** the v2.7.8 originals: as of 2026-11-04, 16 of the 23
> copies have been edited so that they load in BEAST 3 (for example, `TreeHeightLogger` was
> replaced by `TreeStatLogger`). They are not tested; always take the BEAST 2 XML from the beast2
> repo (tag `v2.7.8`).

In short: each test is a **pair** — a top-level BEAST 2 example and the top-level BEAST 3 file
with the same name. A BEAST 2 example without a BEAST 3 partner is run with BEAST 2 only and
reported as "not converted" until someone converts it.

Rules:

- **BEAST 2 XML**: download it from the beast2 repo at tag
  [`v2.7.8`](https://github.com/CompEvol/beast2/tree/v2.7.8/examples), not from `master` and not
  from beast3 `examples/legacy/` (which may have been edited). Exceptions: testSeqGen and
  testSimulatedAlignment at v2.7.8 don't load in BEAST 2.7 (stale `beast.app.seqgen` class names);
  use the copies fixed in [beast2#1227](https://github.com/CompEvol/beast2/pull/1227). For
  testUCLNclock.json use the copy with explicit sequences from
  [beast2#1228](https://github.com/CompEvol/beast2/pull/1228) (same data, identical traces in 2.7.7).
- **BEAST 3 XML**: only a file at the top level of the beast3 `examples/` folder counts as
  converted (or, for testSeqGen and testSimulatedAlignment, of the beast-fx `examples/` folder). A file with the same name in `legacy/` or `beast2vs1/` does **not** count.
- **Data**: every top-level BEAST 2 example has its alignment inline in the XML (none reads
  from `fasta/` or `nexus/`), so each XML can be copied into `beast2/xml/` on its own. New BEAST 3
  conversions must also be self-contained; if one does need an external data file, copy that
  file next to the XML in `beast3/xml/` and note it in the report.
- New XMLs made with BEAUti (see [ASSIGNMENTS.md](ASSIGNMENTS.md)) go in `beast2/xml/` and `beast3/xml/` here, at the top
  level, with a name that does not clash with an example.

Who does what: see [ASSIGNMENTS.md](ASSIGNMENTS.md).

## Software versions

| Tool    | Version | Where to get it |
|---------|---------|-----------------|
| BEAST 2 | 2.7.9   | Install BEAST 2.7.7, then replace its packages by hand with BEAST.base 2.7.9 and BEAST.app 2.7.8: see [Installing BEAST 2.7.9](#installing-beast-279). 2.7.9 fixes a wrong Hastings ratio in the AVMN operator ([beast2#1219](https://github.com/CompEvol/beast2/issues/1219)); none of the examples use AVMN, but the BEAUti track does |
| BEAST 3 | `v2.8.0-rc2` | macOS: `BEAST.v2.8.0-rc2.dmg` from <https://github.com/CompEvol/beast3/releases/tag/v2.8.0-rc2>. RC2 has no Linux or Windows download; there, build from source at tag `v2.8.0-rc2` with JDK 25 + Maven (`git checkout v2.8.0-rc2`, `mvn package -Dmaven.test.skip=true`, then `bin/beast`) |

Record the exact BEAST 3 release tag **or** git commit hash in the report — results are only meaningful against a fixed version.

This round of testing is on macOS: all BEAUti-track testers use Macs. Windows and Linux get a
separate round of tests later. The chains can run on your own machine or on NeSI (Linux); see
[Step 2](#step-2--run-beast-2-and-beast-3--2-replicates-each).

### Installing BEAST 2.7.9

There is no 2.7.9 or 2.7.8 installer: the newest is 2.7.7, which is what
<https://www.beast2.org> links to, and the v2.7.8 release has only package zips. BEAST.base 2.7.9
is not on the package server yet, so `packagemanager -add BEAST.base -version 2.7.9` fails with
"Package version 2.7.9 is not available". So build the reference by hand: the 2.7.7 installer,
with **BEAST.base 2.7.9** from the
[`v2.7.9pre`](https://github.com/CompEvol/beast2/releases/tag/v2.7.9pre) release and
**BEAST.app 2.7.8** from the [`v2.7.8`](https://github.com/CompEvol/beast2/releases/tag/v2.7.8)
release. That is BEAST 2.7.8 with BEAST.base updated to 2.7.9. The AVMN fix is entirely in
BEAST.base; there is no BEAST.app 2.7.9.

On macOS:

1. Install `BEAST.v2.7.7.Mac.dmg` from <https://github.com/CompEvol/beast2/releases/tag/v2.7.7>
   (it bundles its own Java), then run it once so that it creates the user package directory:

   ```bash
   B="/Applications/BEAST 2.7.7/bin"
   "$B/beast" -version
   ```

2. Replace `BEAST.base` and `BEAST.app` in the user package directory:

   ```bash
   cd "$HOME/Library/Application Support/BEAST/2.7"
   rm -rf BEAST.base BEAST.app && mkdir BEAST.base BEAST.app
   curl -LO https://github.com/CompEvol/beast2/releases/download/v2.7.9pre/BEAST.base.package.v2.7.9.zip
   curl -LO https://github.com/CompEvol/beast2/releases/download/v2.7.8/BEAST.app.package.v2.7.8.zip
   unzip -q BEAST.base.package.v2.7.9.zip -d BEAST.base && unzip -q BEAST.app.package.v2.7.8.zip -d BEAST.app
   rm BEAST.base.package.v2.7.9.zip BEAST.app.package.v2.7.8.zip
   ```

3. Check that it works:

   ```bash
   "$B/beast" -version
   ```

   It must print `BEAST.base v2.7.9` and `BEAST.app v2.7.8`. The first line still says
   `BEAST v2.7.7`, because that is the version of the launcher; ignore it. If it stops with
   `UnsupportedClassVersionError`, you downloaded the broken BEAST.base zip that was on
   `v2.7.9pre` until the afternoon of 5 Nov; download it again. In `"$B/packagemanager" -list`
   the "Latest Version" column for BEAST.base says 2.7.8. Don't upgrade BEAST.base from the
   package manager, which would take it back to 2.7.8.

4. Install ORC and bModelTest as usual (`"$B/packagemanager" -add ORC`, `-add bModelTest`, or
   File › Manage Packages in BEAUti). ORC also installs BEASTLabs. None of them changes
   BEAST.base or BEAST.app. Run `"$B/beast" -version` again and record the package versions it
   lists.

The user package directory is shared by every BEAST 2.7.x on the machine, so after this every
BEAST 2.7 install you start, BEAUti included, uses these packages. Once BEAST.base 2.7.9 is on
the package server, `packagemanager -add BEAST.base -version 2.7.9` replaces the BEAST.base part
of step 2.

On NeSI, the same steps apply with `BEAST.v2.7.7.Linux.x86.tgz` and `~/.beast/2.7` (see
[Step 2](#step-2--run-beast-2-and-beast-3--2-replicates-each)).

## Example inventory

Status as of 2026-11-09. `*.state` and editor backup files (`testHKY.xml~`) are excluded.
"Converted" means a file of the same name exists at the top level of the beast3 examples folder,
except testSeqGen and testSimulatedAlignment, which need beast-fx and moved to
`beast-fx/src/test/resources/beast.fx/examples/` in beast3#204. "Converted in" is blank for the 18
examples converted before this round.

| # | BEAST 2 example | Converted to BEAST 3? | Converted in | Notes |
|---|-----------------|:---------------------:|:------------:|-------|
| 1 | bitflip.xml | yes |  |  |
| 2 | testBSP.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 3 | testCalYule_5t_2c.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 4 | testCalibration.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 5 | testClassicRootCalibrationPrior.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 6 | testCoalescent.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 7 | testConditionalRootCalibrationPrior.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 8 | testDirectSimulator.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) | simulator, no MCMC posterior |
| 9 | testDirectSimulator2.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) | simulator, no MCMC posterior |
| 10 | testDirectSimulatorHierarchical.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) | simulator, no MCMC posterior |
| 11 | testEBSP.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 12 | testExponentialGrowth.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 13 | testGTR.xml | yes |  |  |
| 14 | testHKY.json | yes |  | JSON input |
| 15 | testHKY.xml | yes |  |  |
| 16 | testJukesCantor.xml | yes |  |  |
| 17 | testJukesCantorShort.xml | yes |  |  |
| 18 | testJukesCantorShortUncertain.xml | yes |  |  |
| 19 | testJukesCantorShortUncertain2.xml | yes |  |  |
| 20 | testJukesCantorShortUncertain2MLE.xml | yes |  |  |
| 21 | testMultipleAlignments_randomTaxaOrder.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) |  |
| 22 | testOpSubSchedule.xml | yes |  |  |
| 23 | testPlates.xml | yes |  |  |
| 24 | testRNA.xml | yes |  |  |
| 25 | testRandomLocalClock.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) |  |
| 26 | testRelaxedClock.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) |  |
| 27 | testRestrictedGTR.xml | yes |  |  |
| 28 | testSRD06.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) |  |
| 29 | testSYM.xml | yes |  |  |
| 30 | testSeqGen.xml | yes, in beast-fx | [beast3#204](https://github.com/CompEvol/beast3/pull/204) | simulator, no MCMC posterior |
| 31 | testSimulatedAlignment.xml | yes, in beast-fx | [beast3#204](https://github.com/CompEvol/beast3/pull/204) | simulates data, then runs MCMC |
| 32 | testSliceHKY.xml | **no** |  | uses `SliceOperator`, which BEAST 3 doesn't have; exclude or port (open question in ASSIGNMENTS) |
| 33 | testStarBeast.xml | excluded |  | *BEAST 1, code not migrated to BEAST 3 |
| 34 | testStarBeastFBD.xml | excluded |  | *BEAST 1, code not migrated to BEAST 3 |
| 35 | testTIM.xml | yes |  |  |
| 36 | testTN93.xml | yes |  |  |
| 37 | testTVM.xml | yes |  |  |
| 38 | testTipDates.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) |  |
| 39 | testTipDates2.xml | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) |  |
| 40 | testTwoCalibrationsPrior.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 41 | testUCLNclock.json | yes | [beast3#204](https://github.com/CompEvol/beast3/pull/204) | JSON input |
| 42 | testYuleCalibrated.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |
| 43 | testYuleOneSite.xml | yes |  |  |
| 44 | testYuleUncalibrated.xml | yes | [beast3#199](https://github.com/CompEvol/beast3/pull/199) |  |

**Excluded:** the *BEAST 1 examples (`testStarBeast.xml`, `testStarBeastFBD.xml`) are excluded because the *BEAST 1 code was not migrated to BEAST 3.

Summary: 44 examples, 2 excluded, 42 to test: 41 converted (18 before this round, 11 in beast3#199,
12 in beast3#204) and 1 not converted (testSliceHKY).

To regenerate the lists:

```bash
gh api repos/CompEvol/beast2/contents/examples \
  --jq '.[] | select(.type=="file") | .name'
gh api repos/CompEvol/beast3/contents/beast-base/src/test/resources/beast.base/examples \
  --jq '.[] | select(.type=="file") | .name'
gh api repos/CompEvol/beast3/contents/beast-fx/src/test/resources/beast.fx/examples \
  --jq '.[] | select(.type=="file") | .name'
```

## Proposed repository layout

```
beast3-test/
├── README.md
├── beast2/
│   ├── xml/                       # copies of the BEAST 2 v2.7.8 example XMLs used
│   └── log/<example>/rep<N>/     # *.log, *.trees, beast.out
├── beast3/
│   ├── xml/                       # copies of the BEAST 3 converted XMLs used
│   └── log/<example>/rep<N>/
├── nesi/                          # Slurm job scripts
└── reports/
    ├── model-check.md     # step 1 results
    ├── summary/           # LogAnalyser output, comparison tables
    └── REPORT.md          # final report (step 5)
```

Commit the exact XMLs that were run (do not rely on upstream `master`, which may change).
`*.log` files and stdout are small enough to commit.

**Tree files (`*.trees`) don't go in git.** Upload them to the shared Dropbox folder
`beast3-test` (<https://www.dropbox.com/home/beast3-test>), in the same layout as this repo,
e.g. the trees of `beast2/log/C01/rep1/` go in `beast3-test/beast2/log/C01/rep1/`. The parameter log (`*.log`) is
enough for the parameter comparison in step 4; the clade and tMRCA comparison needs the trees.

## Tester instructions

### Step 1 — Check that the BEAST 3 model matches the BEAST 2 XML

For every converted example, diff the BEAST 2 and BEAST 3 XMLs side by side and confirm
each of the following is equivalent (names/classes may differ because BEAST 3 uses the new
strongly typed `beast.base.spec` classes — check the *meaning*, not the spelling):

- [ ] Data: same alignment(s), taxa, sequence type, tip dates, partitions / filters
- [ ] Site model: substitution model, frequencies, gamma categories, proportion invariant
- [ ] Clock model: strict / relaxed / random local, and its parameters
- [ ] Tree prior: Yule, birth–death, coalescent, BSP/EBSP, calibrations / MRCA priors
- [ ] Priors: every parameter has the same distribution with the same hyper-parameters, bounds and initial value
- [ ] Parameters that are estimated vs fixed are the same
- [ ] Operators: same set of parameters operated on (weights may differ; note any differences)
- [ ] MCMC: same `chainLength`; loggers record the same quantities with the same `logEvery`

Record the result per example in `reports/model-check.md` as **match**, **match with minor
differences** (list them) or **mismatch** (list them, and raise an issue on
<https://github.com/CompEvol/beast3/issues>). Mismatches must be resolved before step 2,
otherwise the posterior comparison is meaningless.

Also produce a **parameter name mapping** (BEAST 2 log column → BEAST 3 log column) for
each example; step 4 needs it.

For unconverted examples, only run BEAST 2 (step 2) and mark them "not converted" in the report.
For the simulator examples (no MCMC), only check that both versions run without error.

### Step 2 — Run BEAST 2 and BEAST 3 (≥ 2 replicates each)

Run on your own machine or on NeSI. The posterior doesn't depend on where a chain runs, so the
rules below are what matters, not the machine. Most examples finish in minutes on a laptop.
NeSI helps with the long chains (testEBSP, testRandomLocalClock) and with running many replicates
at once.

On NeSI, install both versions in your project directory:

```bash
cd /nesi/project/<project_code>/$USER
wget https://github.com/CompEvol/beast2/releases/download/v2.7.7/BEAST.v2.7.7.Linux.x86.tgz
tar xzf BEAST.v2.7.7.Linux.x86.tgz && mv beast beast2.7.9
beast2.7.9/bin/beast -version     # creates ~/.beast/2.7
# replace BEAST.base (2.7.9) and BEAST.app (2.7.8) in ~/.beast/2.7 (see "Installing BEAST 2.7.9"), then:
beast2.7.9/bin/beast -version     # must list BEAST.base v2.7.9 and BEAST.app v2.7.8

# BEAST 3: RC2 has no Linux download, so build it from source with JDK 25 + Maven
git clone https://github.com/CompEvol/beast3.git && cd beast3 && git checkout v2.8.0-rc2
mvn package -Dmaven.test.skip=true && bin/beast -version   # prints "BEAST v2.8.0 rc2"
```

Rules for every run:

- Run each replicate in **its own directory** (`<beast2|beast3>/log/<example>/rep<N>/`), so log files never overwrite each other.
- Use a different, recorded seed per replicate: e.g. rep1 `-seed 1`, rep2 `-seed 2`. Use the same seeds for BEAST 2 and BEAST 3.
- Do not change `chainLength`; if an example's chain is too short to reach ESS ≥ 200, increase it **identically** in both versions and record it.
- Keep stdout/stderr (`beast.out`) — it contains the start/end state and run time.
- Record the exact versions: the BEAST 3 tag or commit (a local build of a branch is fine; name
  its commit), the BEAST 2 package versions from `beast -version`, and the Java version.
  Record also where the runs ran: your machine and OS, or NeSI.
- Keep the XML exactly as run in each replicate directory if you changed `chainLength` or
  `logEvery`.
- If you report run times, time runs that did not share the machine with other runs.

On NeSI, an example Slurm array script can be shared on request.


### Step 3 — Collect logs

- Copy the `*.log` and `beast.out` files into `beast2/log/` and `beast3/log/` (from NeSI, copy them back or commit directly there).
  Upload the `*.trees` files to the Dropbox folder `beast3-test` at the same path (see
  [Proposed repository layout](#proposed-repository-layout)), not to git.
- Check every `beast.out` finished normally (no exception, final "End likelihood" line present). List failed runs in the report with the error message.
- Commit and push to this repo, with the commit message naming the BEAST versions used.

### Step 4 — Compare the posteriors of the main parameters

For each converted example, compare at least `posterior`, `likelihood`, `prior`, tree height /
tree length, and every estimated model parameter (substitution rates, frequencies, gamma
shape, clock rate, birth rate, population size, …) using the mapping from step 1.

1. Summarise each log with 10 % burn-in, e.g. with LogAnalyser from either version:
   ```bash
   beast2.7.9/bin/loganalyser -b 10 beast2/log/testHKY/rep1/testHKY.log
   ```
   or load the logs into Tracer. Save the summaries to `reports/summary/`.
2. **Convergence**: ESS ≥ 200 for every compared parameter in every replicate. If not, rerun longer (see step 2) before comparing.
3. **Replicate agreement (baseline)**: the replicates of the same version should agree with each other; this shows the expected run-to-run noise.
4. **BEAST 2 vs BEAST 3**: combine replicates per version (`logcombiner -b 10 -log <example>/rep1/x.log -log <example>/rep2/x.log -o <example>/combined.log`), then for each parameter:
   - the posterior means agree within Monte Carlo error: |mean₂ − mean₃| / √(se₂² + se₃²) < 3, where se = sd / √ESS;
   - the 95 % HPD intervals substantially overlap;
   - optionally, overlay the marginal densities in Tracer and save a screenshot.
5. Classify each example as **matched**, **borderline** (one parameter just outside the threshold — rerun with longer chains to confirm) or **not matched**.

#### Comparing results

`scripts/compare.py` does items 1–5 in one step (Python 3, no extra packages needed). Run it from
the repository root:

```bash
python3 scripts/compare.py testHKY            # beast2/log/testHKY vs beast3/log/testHKY
python3 scripts/compare.py beauti-C07 -b 10   # BEAUti track; -b = burn-in %
python3 scripts/compare.py --all              # every name logged in both versions, one summary table
python3 scripts/compare.py --name beauti-C30-resume --a <resumed run dirs> --label-a resumed \
        --b <uninterrupted run dirs> --label-b uninterrupted
```

It writes `reports/summary/<name>.md` (tables, findings and verdict) and `<name>.tsv`. ESS and HPD
match LogAnalyser. Columns are matched by name; for renamed columns, put
`<beast2 column><TAB><beast3 column>` lines in `reports/maps/<name>.tsv`. `--help` lists all options.

### Step 5 — Report

Write `reports/REPORT.md` containing:

- BEAST 2 and BEAST 3 versions (tag/commit), Java version, where the runs ran (machine and OS, or NeSI), date, seeds, burn-in.
- One summary table covering all 42 tested examples (list the 2 excluded *BEAST 1 examples separately):

  | Example | Converted | Model check | BEAST 2 ran | BEAST 3 ran | Min ESS | Posterior matched | Notes |
  |---------|-----------|-------------|-------------|-------------|---------|-------------------|-------|
  | testHKY.xml | yes | match | ✓ | ✓ | 1520 | matched | |

- For every converted example, a per-parameter table: mean, 95 % HPD and ESS for BEAST 2 and BEAST 3, and the z-score from step 4.
- A list of problems found (model mismatches, failed runs, unmatched posteriors), each linked to a GitHub issue on beast3 where one was raised.
- The list of examples still to be converted.

## BEAUti by hand and core model coverage

The example XMLs only test the XML → MCMC path. Real users start in BEAUti, and the examples
don't cover every core model. Both gaps are covered by the BEAUti track in
[ASSIGNMENTS.md](ASSIGNMENTS.md): 30 analyses built by hand in BEAUti 2.7.9 and BEAUti 3,
covering every substitution, frequency, clock, tree-prior and starting-tree option in the
BEAST 3 templates. Results go in `reports/beauti-manual.md` and `reports/model-coverage.md`.

The [status site](https://compevol.github.io/beast3-test/) has an overview page stating the goal,
and one page per track: [example XMLs](https://compevol.github.io/beast3-test/examples.html) and
[BEAUti by hand](https://compevol.github.io/beast3-test/beauti.html). `.github/workflows/status-page.yml`
rebuilds it on every push to `main`. The numbers come from `reports/summary/batch-summary.md`, the
BEAUti tester and model from `ASSIGNMENTS.md`, and the example inventory from this README. The
status and one-line note of each entry are set by hand, in `reports/status.tsv` (BEAUti) and
`reports/examples-status.tsv` (examples), and the panels under each table in
`reports/status-notes.md` and `reports/examples-notes.md`. Each page lists any entry whose status
disagrees with the latest numbers. To preview locally, run `python3 scripts/build_status_page.py`
and open `_site/index.html`.
