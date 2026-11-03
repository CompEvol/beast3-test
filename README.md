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

### What to test

Test the `*.xml` / `*.json` files sitting **directly** in each `examples/` folder.
Nothing in a sub-folder is tested, in either repository.

| Repository | Location | What it is | To test? |
|------------|----------|------------|----------|
| beast2 `examples/` | top-level `*.xml` / `*.json` | the BEAST 2 examples (see [Example inventory](#example-inventory)) | ✅ **Yes** — run with BEAST 2.7.8 as the reference |
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
  from beast3 `examples/legacy/` (which may have been edited).
- **BEAST 3 XML**: only a file at the top level of the beast3 `examples/` folder counts as
  converted. A file with the same name in `legacy/` or `beast2vs1/` does **not** count.
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
| BEAST 2 | 2.7.8   | <https://github.com/CompEvol/beast2/releases/tag/v2.7.8> (`BEAST.v2.7.8.Linux.x86_64.tgz`, bundles its own JRE) |
| BEAST 3 | 2.8.0 (currently `v2.8.0-rc1`) or `master` | <https://github.com/CompEvol/beast3/releases> (`BEAST.v2.8.0.Linux.x86_64.tgz`), or build from source with JDK 25 + Maven (`mvn package -Dmaven.test.skip=true`, then `bin/beast`) |

Record the exact BEAST 3 release tag **or** git commit hash in the report — results are only meaningful against a fixed version.

## Example inventory

Status as of 2026-11-03. `*.state` and editor backup files (`testHKY.xml~`) are excluded.
"Converted" means a file of the same name exists at the top level of the beast3 examples folder.

| # | BEAST 2 example | Converted to BEAST 3? | Notes |
|---|-----------------|:---------------------:|-------|
| 1  | bitflip.xml | yes | |
| 2  | testBSP.xml | no | |
| 3  | testCalYule_5t_2c.xml | no | |
| 4  | testCalibration.xml | no | |
| 5  | testClassicRootCalibrationPrior.xml | no | |
| 6  | testCoalescent.xml | no | |
| 7  | testConditionalRootCalibrationPrior.xml | no | |
| 8  | testDirectSimulator.xml | no | simulator, no MCMC posterior |
| 9  | testDirectSimulator2.xml | no | simulator, no MCMC posterior |
| 10 | testDirectSimulatorHierarchical.xml | no | simulator, no MCMC posterior |
| 11 | testEBSP.xml | no | |
| 12 | testExponentialGrowth.xml | no | |
| 13 | testGTR.xml | yes | |
| 14 | testHKY.json | yes | JSON input |
| 15 | testHKY.xml | yes | |
| 16 | testJukesCantor.xml | yes | |
| 17 | testJukesCantorShort.xml | yes | |
| 18 | testJukesCantorShortUncertain.xml | yes | |
| 19 | testJukesCantorShortUncertain2.xml | yes | |
| 20 | testJukesCantorShortUncertain2MLE.xml | yes | |
| 21 | testMultipleAlignments_randomTaxaOrder.xml | no | |
| 22 | testOpSubSchedule.xml | yes | |
| 23 | testPlates.xml | yes | |
| 24 | testRNA.xml | yes | |
| 25 | testRandomLocalClock.xml | no | |
| 26 | testRelaxedClock.xml | no | |
| 27 | testRestrictedGTR.xml | yes | |
| 28 | testSRD06.xml | no | |
| 29 | testSYM.xml | yes | |
| 30 | testSeqGen.xml | no | simulator, no MCMC posterior |
| 31 | testSimulatedAlignment.xml | no | simulates data, then runs MCMC |
| 32 | testSliceHKY.xml | no | not present in beast3 `legacy/` either |
| 33 | testStarBeast.xml | excluded | *BEAST 1, code not migrated to BEAST 3 |
| 34 | testStarBeastFBD.xml | excluded | *BEAST 1, code not migrated to BEAST 3 |
| 35 | testTIM.xml | yes | |
| 36 | testTN93.xml | yes | |
| 37 | testTVM.xml | yes | |
| 38 | testTipDates.xml | no | |
| 39 | testTipDates2.xml | no | |
| 40 | testTwoCalibrationsPrior.xml | no | |
| 41 | testUCLNclock.json | no | JSON input |
| 42 | testYuleCalibrated.xml | no | |
| 43 | testYuleOneSite.xml | yes | |
| 44 | testYuleUncalibrated.xml | no | |

**Excluded:** the *BEAST 1 examples (`testStarBeast.xml`, `testStarBeastFBD.xml`) are excluded because the *BEAST 1 code was not migrated to BEAST 3.

Summary: 44 examples, 2 excluded, 42 to test: 18 converted, 24 not converted. Before starting, re-check both
folders on GitHub and update this table — the beast3 conversion is ongoing.

To regenerate the lists:

```bash
gh api repos/CompEvol/beast2/contents/examples \
  --jq '.[] | select(.type=="file") | .name'
gh api repos/CompEvol/beast3/contents/beast-base/src/test/resources/beast.base/examples \
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
Keep large `*.trees` files out of git unless needed (use Git LFS or compress them);
`*.log` files and stdout are small enough to commit.

> **Note:** if a tree log (`*.trees`) is too large to upload to the repo, leave it out — the
> parameter log (`*.log`) from the MCMC is enough for the comparison in step 4.

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

### Step 2 — Run BEAST 2 and BEAST 3 on NeSI (≥ 2 replicates each)

Install both versions in your NeSI project directory:

```bash
cd /nesi/project/<project_code>/$USER
wget https://github.com/CompEvol/beast2/releases/download/v2.7.8/BEAST.v2.7.8.Linux.x86_64.tgz
tar xzf BEAST.v2.7.8.Linux.x86_64.tgz && mv beast beast2.7.8
# BEAST 3: download the release tgz the same way (rename to beast3), or build from source with JDK 25
```

Rules for every run:

- Run each replicate in **its own directory** (`<beast2|beast3>/log/<example>/rep<N>/`), so log files never overwrite each other.
- Use a different, recorded seed per replicate: e.g. rep1 `-seed 1`, rep2 `-seed 2`. Use the same seeds for BEAST 2 and BEAST 3.
- Do not change `chainLength`; if an example's chain is too short to reach ESS ≥ 200, increase it **identically** in both versions and record it.
- Keep stdout/stderr (`beast.out`) — it contains the start/end state and run time.

Example Slurm array script can be shared as request.


### Step 3 — Collect logs

- Copy back (or commit directly from NeSI) the `*.log`, `beast.out` and, if small, `*.trees` files into `beast2/log/` and `beast3/log/`.
  If a `*.trees` file is too large to upload, skip it; the parameter `*.log` is enough.
- Check every `beast.out` finished normally (no exception, final "End likelihood" line present). List failed runs in the report with the error message.
- Commit and push to this repo, with the commit message naming the BEAST versions used.

### Step 4 — Compare the posteriors of the main parameters

For each converted example, compare at least `posterior`, `likelihood`, `prior`, tree height /
tree length, and every estimated model parameter (substitution rates, frequencies, gamma
shape, clock rate, birth rate, population size, …) using the mapping from step 1.

1. Summarise each log with 10 % burn-in, e.g. with LogAnalyser from either version:
   ```bash
   beast2.7.8/bin/loganalyser -b 10 beast2/log/testHKY/rep1/testHKY.log
   ```
   or load the logs into Tracer. Save the summaries to `reports/summary/`.
2. **Convergence**: ESS ≥ 200 for every compared parameter in every replicate. If not, rerun longer (see step 2) before comparing.
3. **Replicate agreement (baseline)**: the replicates of the same version should agree with each other; this shows the expected run-to-run noise.
4. **BEAST 2 vs BEAST 3**: combine replicates per version (`logcombiner -b 10 -log <example>/rep1/x.log -log <example>/rep2/x.log -o <example>/combined.log`), then for each parameter:
   - the posterior means agree within Monte Carlo error: |mean₂ − mean₃| / √(se₂² + se₃²) < 3, where se = sd / √ESS;
   - the 95 % HPD intervals substantially overlap;
   - optionally, overlay the marginal densities in Tracer and save a screenshot.
5. Classify each example as **matched**, **borderline** (one parameter just outside the threshold — rerun with longer chains to confirm) or **not matched**.

### Step 5 — Report

Write `reports/REPORT.md` containing:

- BEAST 2 and BEAST 3 versions (tag/commit), Java version, NeSI cluster, date, seeds, burn-in.
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
[ASSIGNMENTS.md](ASSIGNMENTS.md): 30 analyses built by hand in BEAUti 2.7.8 and BEAUti 3,
covering every substitution, frequency, clock, tree-prior and starting-tree option in the
BEAST 3 templates. Results go in `reports/beauti-manual.md` and `reports/model-coverage.md`.
