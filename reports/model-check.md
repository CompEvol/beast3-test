# Step 1: model check

For each converted example: does the BEAST 3 XML specify the same model as the BEAST 2.7.8 XML?
See README step 1 for the checklist. Results are **match**, **match with minor differences**, or
**mismatch**.

## Calibrations and tree priors (Alexei)

Converted on 6 Nov 2026, from the beast2 `v2.7.8` originals (not the edited `legacy/` copies),
on beast3 branch `examples/convert-calibrations-treepriors`
([beast3#199](https://github.com/CompEvol/beast3/pull/199), stacked on the fixes in
[beast3#198](https://github.com/CompEvol/beast3/pull/198)).

Ten of the eleven originals sampled with an improper prior on at least one estimated parameter
(see Proper priors below). Both the BEAST 2 examples
([beast2#1225](https://github.com/CompEvol/beast2/pull/1225)) and the conversions (#199) now use
proper priors, so the comparison below is of the corrected examples, run in both versions. Each
was run twice in BEAST 2.7.9 and twice in BEAST 3, with seeds 1 and 2, and compared with
`scripts/compare.py`.

**Runs (README steps 2–3).** The logs, `beast.out`, tree files and the XML as run are in
`beast2/log/<example>/rep<N>/` and `beast3/log/<example>/rep<N>/`.
- **Where:** on one Mac (Apple silicon, macOS 26.6), 6 Nov 2026.
- **XMLs:** BEAST 2 from beast2#1225 (commit `4583c690`); BEAST 3 from #199 (commit `45cf64e`).
- **BEAST 2.7.9:** the 2.7.7 macOS app with BEAST.base 2.7.9 and BEAST.app 2.7.8 (README,
  Installing BEAST 2.7.9), its bundled Java 17.0.5. Patched into BEAST.base: the
  `SampleOffValues` fix ([beast2#1223](https://github.com/CompEvol/beast2/pull/1223)), and for
  testConditionalRootCalibrationPrior also the `CalibratedYuleModel` fix
  ([beast2#1224](https://github.com/CompEvol/beast2/pull/1224)).
  (Replicates 3–4 of testYuleUncalibrated also ran with it; it uses a plain Yule prior, so it
  doesn't matter.)
- **BEAST 3:** a local build of beast3 #198 (`b61fd84`) merged with #203 (`d46a622`, the
  `SampleOffValues` fix); for testConditionalRootCalibrationPrior also #207 (`d9a388f`, the
  `CalibratedYuleModel` fix). Run with Java 26.0.1.
- **Chain lengths:** as in the XMLs, except testEBSP (200M), testCalYule_5t_2c (700k) and
  testConditionalRootCalibrationPrior (400M), which are longer in both versions. testYuleUncalibrated
  has four replicates (seeds 1–4): its first two flagged one column at z = 3.2, so it got one rerun
  with new seeds as the pass criteria say.
- **`logEvery`:** chain length / 5,000 in both versions. Every compared parameter has ESS ≥ 355,
  except the birth rate of testConditionalRootCalibrationPrior and the columns that depend on it
  (see its note).
- **testCalYule_5t_2c:** its XML did not change, so these are the earlier runs (BEAST 3 at
  `b61fd84`, BEAST 2.7.9 unpatched, `logEvery` 140); its model has no `SampleOffValues` and a
  fixed birth rate, so neither fix applies.
- **Run times:** not comparable; several runs shared the machine.

### Conversion rules used throughout

- **Proper priors.** Where the original has an improper prior, both versions now use a proper one:
  - rates, population sizes, birth rates and the EBSP `populationMean`: LogNormal(M=0, S=8) in log
    space (median 1, 95% from 1.6e-7 to 6.4e6). This replaces `OneOnX` (testCalibration,
    testClassicRootCalibrationPrior, testEBSP), `Uniform(0, Infinity)` (testYuleCalibrated,
    testYuleUncalibrated), and no prior at all (testBSP clock rate, testCoalescent and
    testExponentialGrowth popSize, testConditionalRootCalibrationPrior and testTwoCalibrationsPrior
    birth rate);
  - kappa, where it had no prior (testCoalescent, testExponentialGrowth): LogNormal(1, 1.25), the
    BEAUti default;
  - the gamma shape in testBSP: Exponential(1);
  - testBSP's Jeffreys (1/x) prior on the first popSize: an exponential prior with an estimated mean
    (`skyline.popSizeInitialMean`), which has a LogNormal(0, 8) prior.
- **Parameter bounds.** BEAST 3 parameters have a domain (`PositiveReal`, `PositiveInt`, …), not
  `lower`/`upper`. Where the original had an upper bound, the BEAST 2 runs were checked to stay
  far below it (noted per example).
- **Operators.** Each original operator is replaced by its spec equivalent with the same weight
  and tuning (`ScaleOperator` on a tree → `ScaleTreeOperator`, legacy `UpDownOperator` → spec
  `UpDownOperator`, `DeltaExchangeOperator` on frequencies → spec with `rvparameter`). BEAUti's
  new default operator set is not used, so the conversions stay close to the originals.
  The one exception is the subtree slide. The legacy `SubtreeSlide` is deprecated, so it is replaced by
  `kernel.BactrianSubtreeSlide` with the same weight. Its starting `size` is the value its
  auto-tuning converges to in these runs, not the original's Gaussian size, which is 1.6–3.5× too
  large for the Bactrian kernel. In testCalibration, testCoalescent and testExponentialGrowth the
  originals' start of 1.0–1.7 is far too large for a tree of height ≈ 0.06, and tuning never
  recovers within a run ([beast3#200](https://github.com/CompEvol/beast3/issues/200)); those
  three start at 0.006–0.008. beast3's `ExampleDeprecationTest` now fails if a release example
  builds any deprecated class.
- **Loggers.** `TreeHeightLogger` (removed in BEAST 3) → `TreeStatLogger`. The column is renamed;
  see the mapping per example.
- **Log column quirk, not a regression:** both versions log `treeLikelihood.alignment` as
  `treeLikelihood.lignment` and `mrca.age(...)` as `mrca.ge(...)` when `sanitiseHeaders="true"`.

### Bugs found while converting

1. Spec `CalibratedYuleModel` and `CalibratedBirthDeathModel` imported the legacy `MRCAPrior`, so
   they never found the spec MRCA priors next to them. A calibrated Yule prior set up the usual way
   (by BEAUti, or as in testYuleCalibrated) stopped with "could not find any properly configured
   calibrations" and a `NullPointerException`. **This affects the BEAUti track: C08 and C27 use a
   calibrated Yule prior.** BEAST 3 only; fixed in #198. Also: after the `NullPointerException`,
   BEAST 3 exited with status 0.
2. Spec `CalibratedYuleInitialTree` built a legacy `CalibratedYuleModel` internally, which rejects
   spec calibration points, so it failed for every input (testCalYule_5t_2c). BEAST 3 only; fixed in
   #198.
3. `SampleOffValues`, which EBSP uses to redraw switched-off population sizes from their prior,
   returned the wrong Hastings ratio, so EBSP did not sample the posterior
   ([beast3#202](https://github.com/CompEvol/beast3/issues/202),
   [beast2#1222](https://github.com/CompEvol/beast2/issues/1222)). In both versions since 2011;
   fixed in [beast3#203](https://github.com/CompEvol/beast3/pull/203) and beast2#1223. **This
   affects the BEAUti track: C13 uses EBSP, and both its reference and RC2 have the bug.**
4. `CalibratedYuleModel` computed 1 − e^(−λh) directly, so its log density became +∞ once the birth
   rate fell below about 1e-17 (root calibration), and wrong from about 1e-9 with nested
   calibrations. The proper birth-rate prior in testConditionalRootCalibrationPrior reaches such
   rates: BEAST 3 stopped with "positive infinite posterior". In both versions; fixed in
   [beast3#207](https://github.com/CompEvol/beast3/pull/207) and beast2#1224.

### Results

"Max z" is over every compared column.

| Example | Model check | Differences | Log column mapping (BEAST 2 → BEAST 3) | Local comparison |
|---|---|---|---|---|
| testYuleUncalibrated | match | — | `TreeHeight` → `Tree.height`; new `Tree.treeLength` | matched (4 replicates), max z 2.10 |
| testYuleCalibrated | match | — | `TreeHeight` → `Tree.height`; new `Tree.treeLength` | matched, max z 1.32 (needs bug fix 1) |
| testCalYule_5t_2c | match | — | none | matched at 700k steps, max z 2.10 (needs bug fix 2); exact check passes |
| testClassicRootCalibrationPrior | match | — | none | matched, max z 0.65 |
| testConditionalRootCalibrationPrior | match | — | `TreeHeight` → `tree.height` | calibrated root age `cal` matched (z 0.29); exact check passes; see note |
| testTwoCalibrationsPrior | match | — | none | matched, max z 1.63 |
| testCoalescent | match | — | none | matched, max z 1.88 |
| testExponentialGrowth | match | — | none | matched, max z 1.06 |
| testCalibration | match | — | none | matched, max z 1.33 |
| testBSP | match with minor differences | popSize upper bound 38000 and clock.rate upper bound 100 dropped (BEAST 2 maxima: 4800 and 0.0016); group sizes start at 1, not 0 | `treeModel.rootHeight` → `tree.height` | matched, max z 1.91 |
| testEBSP | match with minor differences | kappa upper bound 100 dropped (BEAST 2 maxima: 5.7 and 21.7) | `TreeHeight` columns → `treeModelNNN.height` | matched (200M steps), max z 2.66 (needs bug fix 3) |

**testConditionalRootCalibrationPrior:** there is no sequence data, and the birth rate is informed
only by its LogNormal(0, 8) prior and the 4-taxon tree, so its posterior spans about 20 orders of
magnitude. The scale operator mixes slowly over that range: even at 400M steps the birth rate has
ESS of only 13–63 per replicate, and `posterior` and `cyule`, which depend on it, also have ESS below
200 and z up to 4.9. On a log scale the two versions' birth rates agree in the bulk (median log10
about 0, 5% quantile about −5.7 in both); only the upper tail, which mixes slowest, differs. As
ASSIGNMENTS says, this example is compared on the calibrated root age, which has ESS above 4,000 per
replicate and matches (and follows its calibration exactly, see Analytic checks).

**testEBSP:** before bug fix 3, BEAST 2.7.9, the original XML in BEAST 3 and the conversion gave
three different posteriors for `populationMean` (medians 2.7, 3.5 and 4.9) with the same
data-informed population size. With the fix in both versions and the same proper prior on
`populationMean`, the two versions match on every column.

### Analytic checks

Comparing BEAST 2.7.9 with BEAST 3 cannot catch a bug the two versions share, as `SampleOffValues`
showed ([beast3#202](https://github.com/CompEvol/beast3/issues/202)). Two of these examples have an
exact answer: they have no sequence data and use the calibrated Yule prior with `type="full"`,
which makes the marginal distribution of each calibrated node's age equal to its calibration
density. Both versions reproduce it:

| Example | Exact | Version | Replicates × steps | ESS | Mean (z) | Quantiles 5/25/50/75/95% | KS (5% critical) |
|---|---|---|---|---:|---|---|---|
| testConditionalRootCalibrationPrior: root age | LogNormal(2, 0.2): mean 7.538; 5.318/6.457/7.389/8.456/10.267 | BEAST 2.7.9 | 2 × 400M | 9002 | 7.540 (+0.09) | 5.314/6.439/7.401/8.454/10.273 | 0.0077 (0.0143) |
| | | BEAST 3 | 2 × 400M | 9002 | 7.547 (+0.51) | 5.287/6.466/7.400/8.476/10.300 | 0.0078 (0.0143) |
| testCalYule_5t_2c: age of MRCA(a, b) | Uniform(4, 7): mean 5.5; 4.15/4.75/5.5/6.25/6.85 | BEAST 2.7.9 | 4 × 140M | 18004 | 5.500 (+0.04) | 4.153/4.747/5.503/6.244/6.844 | 0.0046 (0.0101) |
| | | BEAST 3 | 4 × 140M | 18004 | 5.496 (−0.62) | 4.151/4.745/5.498/6.239/6.848 | 0.0060 (0.0101) |

`python3 scripts/check_calibrated_marginals.py` reproduces the table from the runs in
`beast2/log/<example>-analytic/` and `beast3/log/<example>-analytic/`.

- **testConditionalRootCalibrationPrior:** the same runs as in `<example>/` (proper birth-rate
  prior; bug fixes 3 and 4 in both versions).
- **testCalYule_5t_2c:** the XML of #199; BEAST 3 with #198, #203 and #207, BEAST 2.7.9 with
  beast2#1223 and #1224 (neither fix changes this model). With the original 700k steps, BEAST 3 was
  at the edge (z +2.2, KS 0.034 against 0.036); the 140M-step runs above settle it.

**Speed:** on the same machine, testBSP took 130 s in BEAST 3 and 79 s in BEAST 2.7.9 for the same
10M steps (earlier runs with the original `SubtreeSlide` and improper priors, one at a time).

## Examples converted before this round (18)

Run on 9 Nov 2026 on one Mac (Apple silicon), 4 chains at a time, seeds 1 and 2:

- **BEAST 2.7.9:** the v2.7.8 example XMLs from beast2 tag `v2.7.8`, unmodified apart from chain
  length and `logEvery`; BEAST 2.7.7 launcher and bundled Java 17.0.5 with BEAST.base 2.7.9 and
  BEAST.app 2.7.8 (the `v2.7.9pre` zips, README "Installing BEAST 2.7.9"; no patches).
- **BEAST 3:** the converted XMLs and the code at beast3 master `8cb5fd0` (after #214), built
  from source with Java 26.0.1. It prints `BEAST v2.8.0 rc2`.
- **Chain lengths:** as in the XMLs, except the GTR family (testGTR, testRNA, testRestrictedGTR,
  testSYM, testTIM, testTVM: 5M → 7M, as ASSIGNMENTS recommends) and testYuleOneSite (10 → 1M; at 10
  steps it is a smoke test). `logEvery` = chain length / 5,000. testTN93 kept 5M.
- **Column maps:** `TreeHeight` → `Tree.height` for the GTR family (`reports/maps/<example>.tsv`).

| Example | Verdict | Notes |
|---------|---------|-------|
| bitflip | matched | |
| testJukesCantor, testJukesCantorShort, testJukesCantorShortUncertain, testJukesCantorShortUncertain2, testJukesCantorShortUncertain2MLE | matched | max z 2.53; ESS ≥ 3,778 |
| testPlates | matched | max z 0.93 |
| testYuleOneSite | matched | at 1M steps |
| testGTR, testRNA, testRestrictedGTR, testSYM, testTIM, testTN93, testTVM | **matched apart from a constant offset in `prior`** | every model parameter, tree height and clade matches (max clade \|Δp\| 0.004). `prior` and `posterior` are 13.79–13.82 lower in BEAST 3 = log(10⁶): the conversions give the Yule birth rate `Uniform(0, 1e6)` where the originals have `Uniform(0, Infinity)` (log density 0). The birth rate never comes near 10⁶, so the posterior is the same |
| testHKY, testHKY.json, testOpSubSchedule | matched, after a kappa prior change in both versions | The originals have an improper 1/X prior on kappa; the shipped conversions had LogNormal(1, 0.5), which pulled kappa from 30.1 to 17.6. Both versions now use LogNormal(0, 8): the BEAST 3 conversions (beast3 branch `fix/example-kappa-prior`, PR to open) and a BEAST 2 copy of each original with only that prior changed. kappa 29.8 vs 30.0; max z 1.47 (testOpSubSchedule 1.29), max clade \|Δp\| 0.005 |

- **testHKY, testHKY.json, testOpSubSchedule** were rerun on 9 Nov (BEAST 3 rc2, chain lengths as
  in the XMLs, seeds 1 and 2). LogNormal(1, 0.5) is not the BEAUti default for kappa,
  LogNormal(1, 1.25); its 95 % range is 1.0–7.3, so it is strongly informative for these data.
  LogNormal(0, 8) is effectively flat over the range kappa takes, so the posterior matches the
  original's (kappa ≈ 30).
- **testSYM** first flagged `rateAT` at z = 3.03 (one column); per the pass criteria it got one
  rerun with seeds 3 and 4, and with all four replicates nothing but the `prior` offset is flagged.
- **testRNA** is testGTR with the alignment coded as RNA. With the same seed its traces are
  identical, row for row, to testGTR's in both versions, so the RNA data type gives the same
  likelihood as DNA. At 5M steps two BEAST 2 frequency columns had ESS < 200, so it was rerun at 7M.
- Reports: `reports/summary/<example>.md`; runs in `beast2/log/<example>/` and
  `beast3/log/<example>/` (testHKY.json as `testHKY-json`).

## Backward compatibility: v2.7.8 XMLs in BEAST 3

Every v2.7.8 example XML, unmodified (2,000-step copies), was loaded in BEAST 3 master `8cb5fd0` on
9 Nov. The result is the same as on 4 Nov: 9 of 44 load (bitflip, testCalYule_5t_2c,
testClassicRootCalibrationPrior, testCoalescent, testExponentialGrowth, testTwoCalibrationsPrior,
and the three DirectSimulator files). The rest fail on `TreeHeightLogger` (31), the
`beast.app.seqgen.*` classes (testSeqGen, testSimulatedAlignment), `SliceOperator` (testSliceHKY)
and the JSON sequence format (testUCLNclock.json).

The six that load and run MCMC were run in both versions from the same unmodified XML (BEAST 2
settings as above; chain lengths as in the XMLs, testCalYule_5t_2c at 700k), two replicates each:

| Example | Verdict | Max z | Min ESS |
|---------|---------|------:|--------:|
| bitflip | matched | 0 | 3,510 |
| testCalYule_5t_2c | matched | 2.93 | 355 |
| testClassicRootCalibrationPrior | matched | 1.46 | 3,624 |
| testCoalescent | matched | 0.41 | 1,187 |
| testExponentialGrowth | matched | 2.39 | 1,540 |
| testTwoCalibrationsPrior | matched | 1.65 | 3,788 |

Four of these originals have an improper prior on at least one parameter (see Proper priors above),
so for them "matched" says the two versions behave the same over these chain lengths, not that a
proper posterior was sampled. Reports: `reports/summary/<example>-v278.md`; runs in
`beast2/log/<example>-v278/` and `beast3/log/<example>-v278/` (bitflip's BEAST 2 runs are those in
`beast2/log/bitflip/`, from the same XML).
