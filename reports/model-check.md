# Step 1: model check

For each converted example: does the BEAST 3 XML specify the same model as the BEAST 2.7.8 XML?
See README step 1 for the checklist. Results are **match**, **match with minor differences**, or
**mismatch**.

## Calibrations and tree priors (Alexei)

Converted on 6 Nov 2026, from the beast2 `v2.7.8` originals (not the edited `legacy/` copies),
on beast3 branch `examples/convert-calibrations-treepriors`
([beast3#199](https://github.com/CompEvol/beast3/pull/199), stacked on the fixes in
[beast3#198](https://github.com/CompEvol/beast3/pull/198)). Each XML was then run twice in
BEAST 2.7.9 and twice in BEAST 3, with seeds 1 and 2, and compared with `scripts/compare.py`.
The BEAST 3 runs were repeated after the subtree slide was switched to `BactrianSubtreeSlide`
(see Operators below); the results table is from those runs.

**Runs (README steps 2–3).** The logs, `beast.out`, tree files and the XML as run are in
`beast2/log/<example>/rep<N>/` and `beast3/log/<example>/rep<N>/`, for every example except
testEBSP, which is being rerun (see its note below).
- **Where:** on one Mac (Apple silicon, macOS 26.6), 6 Nov 2026.
- **BEAST 2.7.9:** the 2.7.7 macOS app with BEAST.base 2.7.9 and BEAST.app 2.7.8 (README,
  Installing BEAST 2.7.9), its bundled Java 17.0.5.
- **BEAST 3:** a local build of beast3 commit `b61fd84` (`v2.8.0-rc2` plus the fixes in #198),
  run with Java 26.0.1. The XMLs are those of #199.
- **Chain lengths:** as in the XMLs, except testCalYule_5t_2c (700k) and
  testConditionalRootCalibrationPrior (40M), which are longer in both versions as ASSIGNMENTS
  says.
- **`logEvery`:** the same in both versions, except testBSP and testCalibration (2,000 in
  BEAST 2.7.9, 1,000 in BEAST 3). It is chain length / 5,000 except in testBSP and
  testCalibration (BEAST 3), testClassicRootCalibrationPrior and testTwoCalibrationsPrior
  (100 instead of 200), and testYuleCalibrated and testYuleUncalibrated (1,000 instead of
  2,000). Every compared parameter except those of testConditionalRootCalibrationPrior has
  ESS ≥ 279.
- **Start sizes:** testCalibration, testCoalescent and testExponentialGrowth ran with the
  subtree slide's earlier start sizes (0.026–0.029, against 0.0063–0.0083 in the final #199
  files). The size is tuned during the run, so the posterior does not depend on it.
- **Run times:** not comparable; several runs shared the machine.

### Conversion rules used throughout

- **1/x prior.** BEAST 3 has no spec `OneOnX`. It is replaced by `LogUniform` on [1e-8, 1e8],
  whose density is proportional to 1/x on that range. In every example that uses it, the posterior
  of the parameter is proper and far inside these bounds, so the posterior is the same. The
  `prior` and `posterior` log columns are lower by the constant ln(ln(1e16)) = 3.607, so
  `compare.py` flags those two columns; every other column must match. Affects testCalibration,
  testClassicRootCalibrationPrior and testEBSP.
- **Uniform(0, ∞) prior.** Its log density in BEAST 2 is 0, and spec `Uniform` rejects an infinite
  bound, so the prior is left out. The parameter's `PositiveReal` domain keeps it positive.
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

Both were in BEAST 3 `v2.8.0-rc2` and are fixed on beast3 branch
`fix/calibrated-yule-spec-mrcaprior` ([beast3#198](https://github.com/CompEvol/beast3/pull/198)),
which the conversions need:

1. Spec `CalibratedYuleModel` and `CalibratedBirthDeathModel` imported the legacy `MRCAPrior`, so
   they never found the spec MRCA priors next to them. A calibrated Yule prior set up the usual way
   (by BEAUti, or as in testYuleCalibrated) stopped with "could not find any properly configured
   calibrations" and a `NullPointerException`. **This affects the BEAUti track: C08 and C27 use a
   calibrated Yule prior.**
2. Spec `CalibratedYuleInitialTree` built a legacy `CalibratedYuleModel` internally, which rejects
   spec calibration points, so it failed for every input (testCalYule_5t_2c).

Also: after the `NullPointerException` in (1), BEAST 3 exited with status 0.

### Results

| Example | Model check | Differences | Log column mapping (BEAST 2 → BEAST 3) | Local comparison |
|---|---|---|---|---|
"Max z" is over every compared column except `posterior` and `prior`.

| Example | Model check | Differences | Log column mapping (BEAST 2 → BEAST 3) | Local comparison |
|---|---|---|---|---|
| testYuleUncalibrated | match with minor differences | Uniform(0, ∞) priors on birthRate and clockRate left out | `TreeHeight` → `Tree.height`; new `Tree.treeLength` | matched, max z 1.60 |
| testYuleCalibrated | match with minor differences | Uniform(0, ∞) prior on clockRate left out | `TreeHeight` → `Tree.height`; new `Tree.treeLength` | matched, max z 2.00 (needs fix 1) |
| testCalYule_5t_2c | match | — | none | matched at 700k steps, max z 2.10 (needs fix 2) |
| testClassicRootCalibrationPrior | match with minor differences | 1/x prior on birthRate → LogUniform | none | matched, max z 1.20, apart from the constant `posterior` offset of −3.60 |
| testConditionalRootCalibrationPrior | match | — | `TreeHeight` → `tree.height` | calibrated root age `cal` matched (z 0.08); nothing else converges in either version, see note |
| testTwoCalibrationsPrior | match | — | none | matched, max z 0.69 |
| testCoalescent | match | — | none | matched, max z 0.13 |
| testExponentialGrowth | match | — | none | matched, max z 0.85 |
| testCalibration | match with minor differences | 1/x prior on popSize → LogUniform | none | matched, max z 1.30, apart from the constant `prior`/`posterior` offset of −3.58 |
| testBSP | match with minor differences | popSize upper bound 38000 and clock.rate upper bound 100 dropped (BEAST 2 maxima: 4800 and 0.0016); group sizes start at 1, not 0 | `treeModel.rootHeight` → `tree.height` | matched, max z 2.00 |
| testEBSP | match with minor differences | 1/x prior on populationMean → LogUniform; kappa upper bound 100 dropped (BEAST 2 maxima: 5.7 and 21.7) | `TreeHeight` columns → `treeModelNNN.height` | **not validated**: `populationMean` and popSizes about 2× larger in BEAST 3; see note |

**testConditionalRootCalibrationPrior:** the birth rate has no prior (the 1/x prior is commented
out in the original) and there is no data, so its posterior is improper. In both versions it
drifts towards 10⁶, which squeezes the internal nodes so the topology hardly mixes. Compare this
example on the calibrated root age only (as ASSIGNMENTS already says); birthRate, posterior and
the clade frequencies will not converge in either version.

**testEBSP:** compared over 40–50M steps per replicate. The 200M-step runs were stopped at about
40M (2.7.9) and 47M (BEAST 3 with the original `SubtreeSlide`); the `BactrianSubtreeSlide` runs
were 50M.
These agree with 2.7.9:
- the tree likelihood and the coalescent log density;
- all four tree heights;
- `sum(indicators)` (0.58 against 0.65, z 1.6).

These don't agree:
- `populationMean`: 9.0 in 2.7.9 against 17.6–26.5 in BEAST 3;
- most popSizes, which are about twice as large (z 3–4.9);
- `posterior`, which is about 51 lower.

The `posterior` difference follows from the `populationMean` difference: the Exponential prior on
each of the ~80 popSizes has mean `populationMean`, so a larger mean lowers the prior density of
all of them. The question is therefore whether `populationMean` differs. In BEAST 3 it mixes
poorly: the two replicates with the original `SubtreeSlide` give 12.6 and 40.4. The two 2.7.9
replicates agree with each other (9.3 and 8.7). Several indicators have ESS below 200. The
difference was already there with the original `SubtreeSlide`, so the operator change is not
the cause. Next step: run both versions to the full 200M steps and compare again. If BEAST 3
still differs, check its EBSP prior on popSizes and `populationMean` against 2.7.9's. Related:
[beast3#191](https://github.com/CompEvol/beast3/issues/191) (BEAST 3 against BEAST 1 on this
example).

**Speed:** on the same machine, testBSP took 130 s in BEAST 3 and 79 s in BEAST 2.7.9 for the same
10M steps (original `SubtreeSlide` runs, one at a time).
