# Work assignments

Two tracks run in parallel before the BEAST 3 (2.8.0) release on **3 December 2026**:

| Track | Who | What |
|-------|-----|------|
| Existing examples | Alexei, Walter | Convert and test the BEAST 2 examples, following [README.md](README.md) steps 1–5 (split below) |
| BEAUti by hand | Eva, Haoyuan, Sophie, Yao, Yuan | Build the 30 analyses below by hand in BEAUti, in both BEAST 2.7.9 and BEAST 3, then run and compare them. This also covers core model coverage |

## Existing examples track

The 23 unconverted examples are split by theme. Each person reviews the other's step 1 model checks.

| | Alexei: calibrations and tree priors (11) | Walter: clocks, tip dates, data and simulators (12) |
|---|---|---|
| Convert, then test | testCalYule_5t_2c, testCalibration, testClassicRootCalibrationPrior, testConditionalRootCalibrationPrior, testTwoCalibrationsPrior, testYuleCalibrated, testYuleUncalibrated, testBSP, testCoalescent, testEBSP, testExponentialGrowth | testRandomLocalClock, testRelaxedClock, testUCLNclock.json, testTipDates, testTipDates2, testSRD06, testMultipleAlignments_randomTaxaOrder, testDirectSimulator, testDirectSimulator2, testDirectSimulatorHierarchical, testSeqGen, testSimulatedAlignment |
| Reviews step 1 for | Walter | Alexei |

Shared and automated by a comparison script:

- Test the 18 already-converted examples (README steps 2–4).
- Run all unmodified v2.7.8 example XMLs in BEAST 3 and compare them with BEAST 2.7.9, as a backward-compatibility check.

Run settings, measured with BEAST 3 on 4 Nov:

- Set `logEvery` on every logger to chain length / 5,000, in both versions, and record it. Fewer samples than that make the ESS estimate unreliable.
- These examples need a longer chain in both versions to reach ESS ≥ 200: testEBSP 10M → 200M (about 16 min), testRandomLocalClock 2M → 100M, testConditionalRootCalibrationPrior 1M → 40M, testCalYule_5t_2c 10k → 700k. The GTR family passes at 5M with little margin; 7M is safer. Everything else passes at its current length.
- One replicate of every example takes about 40 CPU-minutes in total. Two replicates in both versions take about 2.5 CPU-hours.
- testConditionalRootCalibrationPrior has no prior on birthRate (the 1/X is commented out). Compare it on the calibrated node age, not on birthRate.

Backward compatibility, checked on 4 Nov and again on 9 Nov (master `8cb5fd0`): only 9 of the 44 v2.7.8 examples load in BEAST 3, and the 6 of those that run MCMC match BEAST 2.7.9 ([model-check.md](reports/model-check.md#backward-compatibility-v278-xmls-in-beast-3)). The beast3 `examples/legacy/` copies were edited to work around this, so they are not the v2.7.8 originals.

The target is the 44 that BEAST 2.7 itself loads. On 10 Nov BEAST 2.7.7 loaded 42: testSeqGen and testSimulatedAlignment still name `beast.app.seqgen.*`, which moved to `beastfx.app.seqgen` in 2.7.0. [beast2#1227](https://github.com/CompEvol/beast2/pull/1227) fixes the two names; with it all 44 load and run in BEAST 2.7.7, and both also run in BEAST 3 (with beast-fx). testSliceHKY is excluded (`SliceOperator` was removed on purpose), so the BEAST 3 target is **43**. With beast3#235 and the fixed copies from beast2#1227 and beast2#1228, BEAST 3 loads all 43.

| Cause | Examples affected | Status (10 Nov) |
|---|---|---|
| `TreeHeightLogger` was removed (beast3 commit `5ed52d0`) | 31, including all converted examples except bitflip | restored as a deprecated class in [beast3#235](https://github.com/CompEvol/beast3/pull/235): with it, 40 of 44 load (42 with beast2#1227) |
| `beast.app.seqgen.*` class names | testSeqGen, testSimulatedAlignment | stale since 2.7.0, BEAST 2.7 fails too; fixed in the XML by beast2#1227 |
| `SliceOperator` doesn't exist in BEAST 3 | testSliceHKY | excluded: removed on purpose (beast3 `b74755d`); CHANGELOG ([beast3#236](https://github.com/CompEvol/beast3/pull/236)) |
| Alignment `taxon=sequence` shorthand (the JSON example's sequences) removed with `Map`/`TreeTipData` (beast3 `a37b3b2`) | testUCLNclock.json | removed on purpose; the example is rewritten with explicit sequences in [beast2#1228](https://github.com/CompEvol/beast2/pull/1228) (identical traces in 2.7.7), and the removal is in the CHANGELOG ([beast3#236](https://github.com/CompEvol/beast3/pull/236)) |

BEAUti 2.7 writes `TreeStatLogger`, so analyses built in BEAUti 2.7 are not affected; hand-written and older XML is.

Still to decide:

- Whether to restore `TreeHeightLogger` as a deprecated alias of `TreeStatLogger` before release, or list its removal in the release notes. The same question applies to the seqgen class names and the JSON sequence format.

- ~~`testHKY.xml` and `testOpSubSchedule.xml` (already converted) replace the 1/X prior on kappa with a LogNormal.~~ Done 9 Nov: both versions now use LogNormal(0, 8) on kappa (also in `testHKY.json`), and they match ([model-check.md](reports/model-check.md)).
- ~~How conversions handle the 1/X prior, which has no exact spec replacement.~~ The conversions use LogNormal(0, 8) in both versions ([model-check.md](reports/model-check.md)). BEAST 2 XML with `OneOnX` still runs in BEAST 3 through the deprecated legacy class; BEAUti 3 doesn't offer it, and for 2.8 XML LogUniform or a wide LogNormal replaces it.
- ~~`testSliceHKY.xml` uses `SliceOperator`, which doesn't exist in BEAST 3. Exclude it, or port the operator.~~ Excluded (10 Nov): `SliceOperator` was removed on purpose, was used only by this example (no BEAUti template, not in BeastFX), and costs several posterior evaluations per move. The release notes should list it as removed. That makes the backward-compatibility target 43 of the 44 examples.

The rest of this page is about the BEAUti track.

## How the BEAUti matrix is built

- **Built by hand, twice.** Every combination is built from scratch in BEAUti 2.7.9 and in BEAUti 3. Nobody copies XML between versions, because the point is to test BEAUti as well as the inference engine. The one exception is C28, which deliberately loads 2.7.9 XML into BEAUti 3.
- **Covers every BEAUti option.** Together the 30 use every substitution model, frequency option, clock model, tree prior and starting tree in the BEAST 3 BEAUti templates (`beast-fx/src/main/resources/beast.fx/fxtemplates/`), plus ORC and bModelTest as packages.
- **Covers the workflows that break most often:** partition linking and splitting, tip dates, MRCA calibrations, sampling from the prior, prior editing, the Operators and MCMC panels, and resuming a run.
- **Spread across areas.** Each tester's six combinations come from different areas, so a tester who falls behind doesn't leave a whole feature area untested. Nobody has more than three slow combinations.
- **Same data in both versions.** All data are example files shipped with both versions (`examples/nexus`, `examples/fasta`).
- **Overlap with the existing-examples track is intended.** This round was designed independently of the existing examples. If a model passes there but fails here, the problem is probably in BEAUti, not in the engine.

## The 30 combinations

Slow combinations (long chains, start them first) are marked 🐢.

### 1 · Nucleotide substitution baselines (single partition)

| ID | Tester | Data | Site model | Clock | Tree prior | Extras | What it exercises |
|----|--------|------|------------|-------|------------|--------|-------------------|
| C01 | Eva | anolis.nex | JC69 | Strict, rate fixed 1.0 | Yule | All defaults | Simple test. Any discrepancy here points to the core likelihood or the operators |
| C02 | Haoyuan | anolis.nex | HKY, Empirical freqs | Strict, fixed | Yule | — | Empirical frequency subtemplate, kappa prior |
| C03 | Sophie | anolis.nex | HKY + Γ4, Estimated freqs | Strict, fixed | Coalescent constant | — | Gamma categories, shape prior, coalescent popSize |
| C04 | Yuan | anolis.nex | GTR + Γ4 + I (estimate pInv) | Strict, fixed | Yule | — | GTR rate priors, proportion invariant with UnitInterval domain |
| C05 | Yao | anolis.nex | TN93, Estimated freqs | Strict, fixed | Birth-Death | — | TN93 kappas, birth-death parameterisation |

### 2 · Partitions, linking and starting trees

| ID | Tester | Data | Site model | Clock | Tree prior | Extras | What it exercises |
|----|--------|------|------------|-------|------------|--------|-------------------|
| C06 | Eva | primate-mtDNA.nex (4 charsets) | HKY + Γ4, unlinked per partition | Strict, linked | Yule, linked tree | — | Partition import, unlinked site models, per-partition log columns |
| C07 | Haoyuan | primate-mtDNA.nex | HKY, linked across all partitions | Strict, unlinked; estimate relative rates | Yule, linked tree | — | Link/unlink buttons, clock rate estimation across partitions |
| C24 | Yao | primate-mtDNA.nex | GTR + Γ4, unlinked | Strict, linked | Yule | “Fix mean substitution rate” on | DeltaExchange on mutation rates (typed inputs changed in BEAST 3) |
| C25 | Yuan | primate-mtDNA.nex | HKY, unlinked | Strict, unlinked | Yule, **unlinked trees** | — | Independent trees per partition, multiple tree logs |
| C22 | Sophie | anolis.nex | HKY | Strict, fixed | Yule | Newick starting tree from [`data/anolis-start.newick`](data/anolis-start.newick) (the shipped anolis.nex_phyml_tree.txt is empty) | NewickTree starting-tree subtemplate |
| C23 🐢 | Haoyuan | anolis.nex | bModelTest + Γ4 + I (bModelTest package) | Strict, fixed | Yule | ClusterTree (UPGMA) starting tree | Site-model averaging from a third-party package, ClusterTree starting tree |

### 3 · Calibrations and time-scaled trees

| ID | Tester | Data | Site model | Clock | Tree prior | Extras | What it exercises |
|----|--------|------|------------|-------|------------|--------|-------------------|
| C08 | Sophie | primate-mtDNA.nex | HKY + Γ4, linked | Strict, estimated rate | Calibrated Yule | MRCA prior on human–chimp, monophyletic, log-normal | CalibratedYule plus MRCA prior and tMRCA logging |
| C09 | Sophie | anolis.nex | HKY | Strict, estimated rate | Yule | Two MRCA priors: one monophyletic (uniform), one not (normal) | Taxon-set editor, monophyly constraint, bounds on calibrations |
| C10 | Eva | RSV2.nex | HKY + Γ4 | Strict, estimated rate | Coalescent constant | Tip dates parsed from taxon names | Tip Dates panel parsing rules and date direction |
| C11 | Haoyuan | Dengue4.env.nex | GTR + Γ4 | Strict, estimated rate | Coalescent exponential | Tip dates | Exponential growth rate prior with sampled tips |
| C12 🐢 | Sophie | Dengue4.env.nex | HKY + Γ4 | Strict, estimated rate | Bayesian Skyline (5 groups) | Tip dates | BSP group sizes, Markov-chained popSizes |
| C13 🐢 | Eva | RSV2.nex | HKY | Strict, estimated rate | Extended Bayesian Skyline | Tip dates | EBSP indicators and popSizes, the EBSP log file |

### 4 · Clock models

| ID | Tester | Data | Site model | Clock | Tree prior | Extras | What it exercises |
|----|--------|------|------------|-------|------------|--------|-------------------|
| C14 🐢 | Yuan | primate-mtDNA.nex | HKY, linked | Random Local Clock | Yule | — | RLC indicators and rates, rate logging in the tree log |
| C15 🐢 | Yao | RSV2.nex | HKY | Random Local Clock | Coalescent constant | Tip dates | RLC on a time-scaled tree with sampled tips |
| C16 🐢 | Yuan | anolis.nex | HKY + Γ4 | ORC relaxed log-normal (ORC package) | Yule | — | ORC relaxed clock in BEAUti, installing a package in BEAST 3 |
| C17 🐢 | Yao | Dengue4.env.nex | GTR + Γ4 | ORC relaxed log-normal (ORC package) | Bayesian Skyline | Tip dates | Relaxed clock with tip dates, the typical virus analysis |

### 5 · Other data types and importers

| ID | Tester | Data | Site model | Clock | Tree prior | Extras | What it exercises |
|----|--------|------|------------|-------|------------|--------|-------------------|
| C18 | Eva | protein.nex | WAG + Γ4 | Strict, fixed | Yule | — | Amino-acid datatype, WAG |
| C19 | Haoyuan | protein.nex | JTT, Empirical freqs | Strict, fixed | Birth-Death | — | JTT, empirical AA frequencies |
| C20 | Sophie | aminoacid.fasta | Blosum62 + Γ4 | Strict, fixed | Coalescent constant | — | FASTA importer, datatype detection |
| C21 | Yao | E15-binary.fasta | MutationDeathModel | Strict, fixed | Yule | — | Binary datatype and the MutationDeath subtemplate |

### 6 · BEAUti mechanics

| ID | Tester | Data | Site model | Clock | Tree prior | Extras | What it exercises |
|----|--------|------|------------|-------|------------|--------|-------------------|
| C26 | Eva | anolis.nex | HKY + Γ4 | Strict, fixed | Yule | **Sample from prior** | Every marginal must match its analytic prior, so a pass doesn't depend on 2.7.9 |
| C27 | Haoyuan | primate-mtDNA.nex | HKY | Strict, estimated | Calibrated Yule | 2 MRCA priors, sample from prior | Calibration/tree-prior interaction, a common source of unexpected induced priors |
| C28 | Yao | Eva's 2.7.9 XML for C06 and C10 | as built | as built | as built | Run in BEAST 3. BEAUti 3 isn't designed to open 2.7 XML: check that File › Load and drag-and-drop refuse it with a clear message ([beast3#229](https://github.com/CompEvol/beast3/pull/229)) | Backward compatibility of BEAUti 2.7.9 XML in BEAST 3 |
| C29 | Yuan | anolis.nex | HKY + Γ4 | Strict, estimated | Yule | Edit priors: kappa → Exponential(mean 5), shape → Uniform(0, 10), birthRate → Gamma(2, 1), clock → Log-normal | Priors panel parametric distribution editors |
| C30 | Yuan | primate-mtDNA.nex | HKY, linked | Strict, fixed | Yule | Edit operator weights, chain length, log intervals and file names. Stop at 50 % and `-resume` | Operators and MCMC panels, state file and resume, compared with an uninterrupted run |

## Assignments

| Tester | Combinations |
|--------|--------------|
| Eva | C01 JC69 baseline · C06 unlinked partitions · C10 tip dates, coalescent · C13 🐢 Extended BSP · C18 WAG protein · C26 sample from prior |
| Haoyuan | C02 HKY empirical · C07 linked sites, unlinked clocks · C11 exponential growth · C19 JTT protein · C23 🐢 bModelTest, UPGMA start · C27 calibrations from prior |
| Sophie | C03 HKY+Γ coalescent · C08 calibrated Yule · C09 two MRCA priors · C12 🐢 Bayesian Skyline · C20 Blosum62 FASTA · C22 Newick start tree |
| Yao | C05 TN93 birth-death · C15 🐢 RLC with tip dates · C17 🐢 relaxed clock + BSP · C21 binary data · C24 fix mean rate · C28 load 2.7.9 XML |
| Yuan | C04 GTR+Γ+I · C14 🐢 random local clock · C16 🐢 relaxed clock · C25 unlinked trees · C29 prior editing · C30 operators and resume |
| Alexei, Walter | Existing examples track (see above) |

## Run protocol

1. **Versions.** BEAST 2.7.9 and the BEAST 3 release candidate at a fixed tag or commit (see README, Software versions). BEAST 2.7.9 is the BEAST 2.7.7 installer with BEAST.base 2.7.9 and BEAST.app 2.7.8 installed by hand (README, [Installing BEAST 2.7.9](README.md#installing-beast-279)), that is, BEAST 2.7.8 with BEAST.base updated to 2.7.9, which fixes a wrong Hastings ratio in the AVMN operator ([beast2#1219](https://github.com/CompEvol/beast2/issues/1219)). There is no 2.7.8 installer. Check that `beast -version` lists BEAST.base v2.7.9 and BEAST.app v2.7.8 before building anything. Install **ORC and bModelTest** through the package manager in both versions, and record the package versions. If a package won't install or load in BEAST 3, record that as a finding.
2. **Build.** Follow the row exactly in each version. Write down every non-default click so the two builds match, and take a screenshot of any panel that looks different between versions. Save as `beauti-C07.xml` in `beast2/xml/` and `beast3/xml/`.
   - **Fallback, only if the 2.7.9 install doesn't work on your Mac:** use plain 2.7.7, and in BEAUti 2.7.7 set the weight of every `AVMNOperator` to 0 on the Operators panel. Its wrong Hastings ratio biases the tree and the parameters proposed with it; without that operator, 2.7.7 targets the correct posterior. Leave AVMN on in BEAST 3. Switch everyone to 2.7.9 at the same time, and record which reference each run used.
3. **Run.** Run 2 replicates per version, on your machine or on NeSI (README step 2), seeds 1 and 2, in `beast2/log/beauti-C07/rep1/` and so on. Size the chain so every logged parameter reaches ESS ≥ 200 in both versions. For the 🐢 combinations, start with about 50 million steps so they don't need extending later in the week.
4. **Don't expect identical traces.** The BEAST 3 default tree operators changed (`UpDownOperator` replaces EpochFlex/TreeStretch), so only distributions are comparable, even with the same seed.
5. **Leave the subtree slide as BEAUti sets it.** Both versions start `BactrianSubtreeSlide` at `size="1.0"`. For a substitution-scale tree that is about 100× too large, and auto-tuning can't shrink it back within a run ([beast3#200](https://github.com/CompEvol/beast3/issues/200)). On such trees, expect the slide to end with low acceptance (often < 5%), and tree ESS to be lower than it could be, **in both versions**. This is not a BEAST 3 regression, so don't report it as one, and don't change the size by hand. Its effect is measured separately, in BEAST 3 only: `scripts/slide_variants.py` makes two copies of every `beast3/xml/` analysis, one that starts the slide at 0.01 (`-slide`) and one that uses `BactrianSubtreeScale` instead ([beast3#214](https://github.com/CompEvol/beast3/pull/214), `-scale`), and they are run centrally (Alexei). Testers don't need to do anything for this. BEAUti 3 will start the slide at 0.01 from the next build ([beast3#201](https://github.com/CompEvol/beast3/pull/201)).
6. **Record speed.** Record wall-clock time and ESS per hour. A large slowdown is a release finding even when the posteriors agree.
7. **Log every BEAUti oddity** in `reports/beauti-manual.md`, even when the run succeeds: crashes, wrong defaults, IDs that differ from 2.7.9, confusing labels. Raise issues on <https://github.com/CompEvol/beast3/issues>.

## Pass criteria

Use README step 4, plus the following:

- **Continuous parameters:** z = |mean₂ − mean₃| / √(se₂² + se₃²) < 3, with se = sd / √ESS, on the combined replicates.
- **Trees:** for every clade with posterior ≥ 0.05 in either version, flag |Δp| > 0.1. Compare root height and every tMRCA.
- **Sample-from-prior runs (C26, C27):** compare each marginal with its analytic prior, not only with 2.7.9.
- **Resume (C30):** the resumed run must match an uninterrupted BEAST 3 run by the same criteria.
- **Reruns:** a flagged result gets one rerun with new seeds before anyone opens an issue.
- **Log column names:** these may differ between versions (e.g. spec parameter IDs). Map them before comparing, and record each renaming as a finding.

Record results per combination in `reports/beauti-manual.md` and the coverage in `reports/model-coverage.md`.

## Timeline

| Dates | Step |
|-------|------|
| Wed 4 – Thu 5 Nov | Confirm the matrix, pin builds, publish BEAST.base 2.7.9, install ORC and bModelTest in both versions, resolve open questions |
| Fri 6 Nov | Runs start. Each tester builds their first combination in both versions as a setup check, then builds and launches their 🐢 combinations so they run over the weekend. Eva saves C06 and C10 from 2.7.9 the same day so Yao can start C28 |
| Mon 9 – Tue 10 Nov | Build and run the remaining combinations. Comparison script ready by Tue 10 Nov |
| Wed 11 Nov | Collate and compare. Launch reruns for anything flagged that evening |
| Thu 12 Nov | Check reruns, write up findings |
| **Fri 13 Nov** | **Sign-off meeting.** Anything unfinished is listed as an exception with an owner and a date |
| 16 Nov – 2 Dec | Fix and retest blockers |
| Thu 3 Dec | Release |

Hands-on time is roughly 1.2–1.8 working days per tester. Building takes 30–50 minutes per combination for both versions together, and comparison about 10 minutes once the script exists. Most of the elapsed time is unattended MCMC.

## rc3 round: the bundled packages

Planned on 12 Nov, to run once rc3 is tagged; dates to be set at the meeting. BEAST 2.8.0 ships five packages inside the installer: **bModelTest, ORC, SA, StarBeast3 and CCD** ([beast3#248](https://github.com/CompEvol/beast3/issues/248)). This round tests them, and tests the core with them installed. It replaces a full rebuild of C01–C30.

### What it answers

1. Do the five bundled packages work in BEAUti 3 and BEAST 3, and give the same answers as in 2.7.9?
2. Does the core still match 2.7.9 with the packages installed by default? A package can add models and templates to BEAUti and change its defaults (SSM, for example, made `Standard_JC` the default substitution model).
3. Do the combinations that did not pass on rc2, or that changed since, now pass?

### How it differs from the first round

- **Everything is built with the rc3 installer as shipped**, with the five packages seeded on first launch; nothing is installed through the package manager in BEAST 3. Each tester's first combination also checks the seeding: the Package Manager lists the five packages with the versions pinned for the release.
- **BEAST 2.7.9 gets the 2.7 versions of the same packages**, installed through the package manager, plus SSM for the GTR comparisons (below). Record every package version in both.
- **18 combinations by hand** (R01–R18): 12 from the first round that need rebuilding, and 6 new ones for the packages. The other 18 combinations of the first round are not rebuilt by hand: their saved BEAST 3 XMLs are rerun on rc3 and compared automatically (Alexei), which tests the engine but not BEAUti.
- **The automated package check** (`packages/check_packages.sh`) runs on rc3 as well: build, unit tests, examples and headless BEAUti scenarios for all five packages.
- Run protocol and pass criteria are as in the first round.

### GTR has a different prior in BEAST 3

Since [beast3#251](https://github.com/CompEvol/beast3/pull/251), BEAUti 3 puts a Dirichlet prior on the GTR rates; BEAUti 2.7.9's core GTR has independent priors. To keep the comparison like for like, the **2.7.9 side of every GTR combination uses SSM's GTR**, which has the same Dirichlet prior (SSM works in 2.7.9; it is not bundled with 2.8.0 because it crashes in BEAST 3). This affects R01, R03, R09 and R10.

### The 18 combinations

Slow combinations are marked 🐢.

| ID | Was | Tester | Data | Model | Why it is in this round |
|----|-----|--------|------|-------|-------------------------|
| R01 | C04 | Eva | anolis.nex | GTR + Γ4 + I, strict fixed, Yule | GTR prior changed (#251) |
| R02 | C08 | Sophie | primate-mtDNA.nex | HKY + Γ4, strict estimated, Calibrated Yule, MRCA prior | Blocked on rc1 and rc2 (fixed by #198) |
| R03 | C11 | Haoyuan | Dengue4.env.nex | GTR + Γ4, strict estimated, coalescent exponential, tip dates | GTR prior changed |
| R04 🐢 | C12 | Sophie | Dengue4.env.nex | HKY + Γ4, strict estimated, Bayesian skyline, tip dates | Rerun needed on rc2 |
| R05 🐢 | C13 | Eva | RSV2.nex | HKY, strict estimated, extended Bayesian skyline, tip dates | Blocked: `SampleOffValues` fix |
| R06 🐢 | C14 | Yuan | primate-mtDNA.nex | HKY, random local clock, Yule | Chains too short on rc2 |
| R07 🐢 | C15 | Yao | RSV2.nex | HKY, random local clock, coalescent constant, tip dates | Blocked: priors differed |
| R08 | C21 | Yao | E15-binary.fasta | MutationDeathModel, strict fixed, Yule | Rerun: priors differed |
| R09 🐢 | C17 | Yuan | Dengue4.env.nex | GTR + Γ4, ORC relaxed, Bayesian skyline, tip dates | GTR prior changed; ORC as bundled |
| R10 | C24 | Sophie | primate-mtDNA.nex | GTR + Γ4 unlinked, fix mean substitution rate | GTR prior changed |
| R11 🐢 | C23 | Haoyuan | anolis.nex | bModelTest + Γ4 + I, UPGMA start | bModelTest as bundled |
| R12 | C29 | Yuan | anolis.nex | HKY + Γ4, edit every prior | Priors panel changed ([#245](https://github.com/CompEvol/beast3/pull/245), [#274](https://github.com/CompEvol/beast3/pull/274)); also try Bounded Real and Offset Real on kappa |
| R13 | new | Eva | bears.nex (SA package, `examples/nexus`) | HKY, strict estimated, **Fossilized Birth Death** with sampled ancestors | SA in BEAUti: tip dates from the names (backward, after the last `_`), origin, sampled-ancestor count in the log |
| R14 | new | Yuan | bears.nex | as R13, **sample from prior** | SA tree prior on its own; compare with 2.7.9 and the FBD prior's known marginals |
| R15 🐢 | new | Haoyuan | 26.nex, 29.nex, 47.nex (core `examples/nexus`) | **StarBeast3** template, species from the Guess dialog (split on `_`) | StarBeast3 in BEAUti: species assignment, multispecies coalescent |
| R16 🐢 | new | Eva | as R15 | StarBeast3 with the relaxed species-tree clock | StarBeast3's clock models |
| R17 | new | Haoyuan | dna.nex | bModelTest + **ORC** relaxed clock + **FBD** (SA) | Three bundled packages in one analysis |
| R18 | new | Yao | one `.trees` file from R01 (BEAST 3, replicate 1; Eva) | Not BEAUti: **TreeAnnotator with CCD0 and CCD1** (CCD), in 2.7.9 and BEAST 3, on the same tree file | Summary trees from the same input must be identical: an exact pass or fail |

| Tester | Combinations |
|--------|--------------|
| Eva | R01 · R05 🐢 · R13 · R16 🐢 |
| Haoyuan | R03 · R11 🐢 · R15 🐢 · R17 |
| Sophie | R02 · R04 🐢 · R10 |
| Yao | R07 🐢 · R08 · R18 |
| Yuan | R06 🐢 · R09 🐢 · R12 · R14 |

Sophie and Yao, who needed more time in the rc2 round, have three combinations each and one slow one; the others have four, with at most two slow ones. R14 is built by Yuan from scratch, independently of Eva's R13, which also checks that two people set up SA the same way. Testers keep the combinations they built in the rc2 round, apart from R01 (C04), which moves from Yuan to Eva, R09 (C17), from Yao to Yuan, and R10 (C24), from Yao to Sophie.

**One dependency:** Yao's R18 needs a tree file from R01. Eva, who was fastest in the rc2 round, has R01 and builds it first, so that R18 can start early.

### To check before the round

- The 2.7 versions of SA and StarBeast3 install in BEAST 2.7.9, and SA's 2.7 package ships `bears.nex`.
- The rc3 installers seed the five packages ([beast3#248](https://github.com/CompEvol/beast3/issues/248), "What is needed" 1–4).
- CCD is in the automated package check (12 Nov).

## Open questions

- C21: confirm that `E15-binary.fasta` ships with BEAST 2.7 and is imported as binary data in both versions.
- The relaxed exponential clock isn't in the matrix. Add ORC's exponential option to C16 or C17 as a variant if time allows.
