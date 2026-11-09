# BEAST 2 example runs

BEAST.base **2.7.9** (prerelease) on **Java 25.0.2**, 12 examples × 4 replicates. These are the BEAST 2
baseline for `reports/beast3-run-report.md`, not BEAST 3 runs.
Run on 2026-11-10 by `scripts/run_examples.sh beast2`. The earlier Java 17 runs are kept in
`beast2/log-java17/`, with their report in `reports/beast2-run-report-java17.md`.

## At a glance

- ✅ **48 / 48 replicates finished.** Every `beast.out` ends with `Done!`, and no run failed.
- ✅ **Java 25 gives the same results as Java 17** (same seeds; see the comparison below).
- ✅ **Java 25 is faster:** 12–45% less run time per example.
- ⚠ **4 of the 8 MCMC examples have a min ESS below 200:** testRandomLocalClock, testRelaxedClock, testTipDates
  and testSimulatedAlignment. They are short example chains and score the same on Java 17, so these are not failures.
- ⚠ **New warning on Java 25:** BEAGLE uses a "restricted method", which a future Java will block (see Warnings).

## Summary

Run time is the range over the 4 replicates, from the "Total calculation time" line in `beast.out`. The direct
simulators don't print one. Sizes are typical per replicate (KB = 1024 B) and match the Java 17 runs to within
about 0.1%. Min ESS is the lowest value over all non-constant columns of all `*.log` files, after 10% burn-in.
⚠ means below 200.

| Example | Type | Done | Run time (s) | `.log` | `.trees` | Min ESS (column, rep) |
|---|---|:-:|--:|--:|--:|---|
| testRandomLocalClock | MCMC | 4/4 | 3.9 – 4.0 | 74 KB | 50 KB | 7 ⚠ (posterior, rep2) |
| testRelaxedClock | MCMC | 4/4 | 2.7 | 183 KB | 2 × 287 KB ¹ | 42 ⚠ (posterior, rep1) |
| testUCLNclock (JSON) | MCMC | 4/4 | 51 – 52 | 3.2 MB | 8.6 MB | 321 (freqParameter.4, rep1) |
| testTipDates | MCMC | 4/4 | 4.5 – 4.6 | 177 KB | 70 KB | 43 ⚠ (likelihood, rep1) |
| testTipDates2 | MCMC | 4/4 | 66 | 274 KB | 508 KB | 652 (freqParameter.2, rep2) |
| testSRD06 | MCMC | 4/4 | 79 – 80 | 257 KB | 508 KB ² | 563 (thirdSites.hky.kappa, rep3) |
| testMultipleAlignments_randomTaxaOrder | MCMC | 4/4 | 498 – 502 | 3.5 MB | 3 × 228 KB ³ | 651 (gammaShape, rep4) |
| testSimulatedAlignment | MCMC | 4/4 | 1.4 – 1.5 | 27 KB | 26 KB | 41 ⚠ (treeLikelihood, rep4) |
| testDirectSimulator | simulator | 4/4 | – | – | 0.6 KB (2 trees) | n/a |
| testDirectSimulator2 | simulator | 4/4 | – | 234 KB (10,000 samples) | – | 8564 (x, rep3) |
| testDirectSimulatorHierarchical | simulator | 4/4 | – | 60 B (1 sample) | – | n/a |
| testSeqGen | simulator | 4/4 | – | – ⁴ | – | n/a |

¹ One substitution tree and one time tree.
² The file is named `beast_.<seed>.trees`, with a stray dot, while the log is `beast_<seed>.log`.
   The file-name pattern in the XML is probably wrong.
³ One tree file per gene (gene1–3).
⁴ No output files. The simulated alignment goes into `beast.out` (about 20 KB).

## Java 25 vs Java 17

Both sets used the same seeds, so a Java change that broke something would show up as different numbers.

| Example | Same numbers? | Posterior check | Run time, Java 17 → 25 |
|---|---|---|--:|
| testRandomLocalClock | ✅ identical up to rounding (≤ 1e-10) | – | 6.3 → 3.9 s (−37%) |
| testRelaxedClock | ✅ identical up to rounding | – | 4.8 → 2.7 s (−45%) |
| testTipDates | ✅ identical up to rounding | – | 7.4 → 4.5 s (−38%) |
| testSRD06 | ✅ identical up to rounding | – | 100 → 80 s (−20%) |
| testUCLNclock | ↪ chains part ways in 2 of 4 reps ⁵ | ✅ matched (max z 0.6) | 68 → 52 s (−24%) |
| testTipDates2 | ↪ chains part ways in 3 of 4 reps ⁵ | ✅ matched (max z 1.2) | 87 → 66 s (−24%) |
| testMultipleAlignments_randomTaxaOrder | ↪ chains part ways ⁵ | ✅ matched (max z 1.9) | 566 → 501 s (−12%) |
| testSimulatedAlignment | ↪ chains part ways in 2 of 4 reps ⁵ | ✅ matched (max z 0.4) | 2.5 → 1.5 s (−41%) |
| testDirectSimulator | ✅ same trees; last digit differs in 2 reps | – | – |
| testDirectSimulator2 | ✅ identical up to rounding (≤ 2e-16) | – | – |
| testDirectSimulatorHierarchical | ✅ byte-identical | – | – |
| testSeqGen | ✅ byte-identical alignments | – | – |

⁵ Java 25 computes some maths functions slightly differently, in the last digit or so. In a long chain, one
   such tiny difference eventually flips an accept/reject step, and after that the two chains follow different
   random paths. This is expected. What matters is that they sample the same posterior, which
   `scripts/compare.py` confirms: every parameter mean agrees (z well below the flag level of 3) and clade
   frequencies differ by at most 0.04.

## Warnings in `beast.err`

None of these stop a run.

| Example | Warning |
|---|---|
| all examples that load BEAGLE (32 reps) | **New on Java 25:** "System::loadLibrary has been called by beagle.BeagleJNIWrapper … Restricted methods will be blocked in a future release unless native access is enabled." BEAST 2.7.9's launcher should add `--enable-native-access=ALL-UNNAMED` before a future Java turns this into an error. |
| testRelaxedClock | mean of distribution for relaxed clock model is not 1.0. State node `ucld.mean` has no operator. |
| testTipDates, testMultipleAlignments_randomTaxaOrder | Loggers appear to have different log frequency. |
| testTipDates2 | no trait specified for some taxa (e.g. Homo_sapiens): assumed to be 1.0. |
| testMultipleAlignments_randomTaxaOrder | State node `popSize.t:gene1` has no operator. |

## beast-fx legacy XMLs: deprecated SiteModel in the sequence simulators (fixed on master)

`testSeqGen.xml` and `testSimulatedAlignment.xml` come from
`beast-fx/src/test/resources/beast.fx/examples/legacy/` in the beast3 repo. They run
`beastfx.app.seqgen.SequenceSimulator` and `beastfx.app.seqgen.SimulatedAlignment`, with the deprecated
BEAST 2 site model written by its full name, `beast.base.evolution.sitemodel.SiteModel`.

| Version | Result |
|---|---|
| BEAST 2.7.9 | ✅ Both run (4/4). |
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

## Setup

- Launcher: `/Applications/BEAST 2.7.7/bin/beast`. Its `-version` output starts with `BEAST v2.7.7`, which is the launcher's own version. The version that runs is **BEAST.base v2.7.9**, from the full list: BEAST v2.7.7, feast v10.6.1, bModelTest v1.3.3, starbeast3 v1.2.1, CCD v1.0.3, SA v2.1.1, BEAST.base v2.7.9, BEASTLabs v2.0.3, BEAST.app v2.7.8, ORC v1.2.1.
- BEAST options: `-working -beagle_SSE -seed <seed>`
- XMLs: copied by `scripts/copy_examples.sh` into `beast2/xml/` on 2026-11-09 from the `legacy/` folders of the examples of `../beast3`, branch `master`, commit 8cb5fd0. testSeqGen and testSimulatedAlignment were then edited to write the deprecated `SiteModel` by its full class name (see the beast-fx section above). Recorded per example in `beast2/log/run_examples.tsv`.
- Java: **25.0.2**. BEAST.base 2.7.9 has no app or launcher of its own yet, so it runs through the launcher of the
  installed BEAST 2.7.7 app. That launcher normally always uses the Java 17 bundled with the app. BEAST 2.7.9 is
  meant to run on Java 25, so the launcher was changed to use the computer's Java 25 instead (the original is
  kept as `bin/beast.orig`). The BEAST and Java versions of every run are recorded in `beast2/log/run_examples.tsv`
  and in `run_info.txt` in each replicate folder.
- Run date: 2026-11-10
- Machine: Darwin 25.6.0 (arm64)
- Replicates: 4 per example, 4 run at a time; seed per replicate in `beast.out`, the same as the BEAST 3 runs
  and the Java 17 runs
- ESS: minimum over all non-constant columns of all `*.log` files in a replicate, 10 % burn-in; ⚠ = below 200

## Replicates

<details>
<summary>All 48 replicates: seed, run time, samples, min ESS</summary>

| Example | Rep | Seed | Status | Run time (s) | Samples | Min ESS | Column (file) |
|---|---|---|---|---|---|---|---|
| testRandomLocalClock | rep1 | 798545320 | completed | 4 | 181 | 17 ⚠ | posterior (test.798545320.log) |
| testRandomLocalClock | rep2 | 337199670 | completed | 4 | 181 | 7 ⚠ | posterior (test.337199670.log) |
| testRandomLocalClock | rep3 | 380329619 | completed | 4 | 181 | 15 ⚠ | posterior (test.380329619.log) |
| testRandomLocalClock | rep4 | 562333788 | completed | 4 | 181 | 21 ⚠ | posterior (test.562333788.log) |
| testRelaxedClock | rep1 | 317721114 | completed | 3 | 901 | 42 ⚠ | posterior (test.317721114.log) |
| testRelaxedClock | rep2 | 870681542 | completed | 3 | 901 | 67 ⚠ | posterior (test.870681542.log) |
| testRelaxedClock | rep3 | 1025853318 | completed | 3 | 901 | 57 ⚠ | posterior (test.1025853318.log) |
| testRelaxedClock | rep4 | 913274257 | completed | 3 | 901 | 69 ⚠ | posterior (test.913274257.log) |
| testUCLNclock | rep1 | 181696971 | completed | 52 | 9001 | 321 | freqParameter.4 (dna.log) |
| testUCLNclock | rep2 | 998153067 | completed | 51 | 9001 | 399 | freqParameter.1 (dna.log) |
| testUCLNclock | rep3 | 1067999948 | completed | 52 | 9001 | 523 | freqParameter.1 (dna.log) |
| testUCLNclock | rep4 | 887198521 | completed | 52 | 9001 | 404 | freqParameter.1 (dna.log) |
| testTipDates | rep1 | 505579092 | completed | 4 | 901 | 43 ⚠ | likelihood (test.505579092.log) |
| testTipDates | rep2 | 712860779 | completed | 5 | 901 | 218 | likelihood (test.712860779.log) |
| testTipDates | rep3 | 766755024 | completed | 5 | 901 | 155 ⚠ | likelihood (test.766755024.log) |
| testTipDates | rep4 | 894497562 | completed | 5 | 901 | 350 | likelihood (test.894497562.log) |
| testTipDates2 | rep1 | 204377550 | completed | 66 | 901 | 671 | freqParameter.1 (beast_204377550.log) |
| testTipDates2 | rep2 | 618627302 | completed | 66 | 901 | 652 | freqParameter.2 (beast_618627302.log) |
| testTipDates2 | rep3 | 547306038 | completed | 66 | 901 | 716 | freqParameter.3 (beast_547306038.log) |
| testTipDates2 | rep4 | 351625106 | completed | 66 | 901 | 674 | freqParameter.2 (beast_351625106.log) |
| testSRD06 | rep1 | 629243466 | completed | 80 | 901 | 764 | firstAndSecondSites.freqParameter.2 (beast_629243466.log) |
| testSRD06 | rep2 | 432746844 | completed | 79 | 901 | 688 | firstAndSecondSites.freqParameter.4 (beast_432746844.log) |
| testSRD06 | rep3 | 542489439 | completed | 80 | 901 | 563 | thirdSites.hky.kappa (beast_542489439.log) |
| testSRD06 | rep4 | 143610653 | completed | 80 | 901 | 710 | tree.height (beast_143610653.log) |
| testMultipleAlignments_randomTaxaOrder | rep1 | 1016715609 | completed | 501 | 9001 | 689 | gammaShape (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testMultipleAlignments_randomTaxaOrder | rep2 | 38423589 | completed | 502 | 9001 | 898 | gammaShape (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testMultipleAlignments_randomTaxaOrder | rep3 | 538607592 | completed | 501 | 9001 | 922 | gammaShape (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testMultipleAlignments_randomTaxaOrder | rep4 | 119857108 | completed | 498 | 9001 | 651 | gammaShape (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testDirectSimulator | rep1 | 783099780 | completed |  | - | n/a | |
| testDirectSimulator | rep2 | 940416248 | completed |  | - | n/a | |
| testDirectSimulator | rep3 | 323272233 | completed |  | - | n/a | |
| testDirectSimulator | rep4 | 213944042 | completed |  | - | n/a | |
| testDirectSimulator2 | rep1 | 73849810 | completed |  | 9000 | 9000 | x (testDirectSimulator2.log) |
| testDirectSimulator2 | rep2 | 606844007 | completed |  | 9000 | 9000 | x (testDirectSimulator2.log) |
| testDirectSimulator2 | rep3 | 436388536 | completed |  | 9000 | 8564 | x (testDirectSimulator2.log) |
| testDirectSimulator2 | rep4 | 892665903 | completed |  | 9000 | 8940 | x (testDirectSimulator2.log) |
| testDirectSimulatorHierarchical | rep1 | 715630407 | completed |  | - | n/a | |
| testDirectSimulatorHierarchical | rep2 | 98674528 | completed |  | - | n/a | |
| testDirectSimulatorHierarchical | rep3 | 102333413 | completed |  | - | n/a | |
| testDirectSimulatorHierarchical | rep4 | 786067856 | completed |  | - | n/a | |
| testSeqGen | rep1 | 55000162 | completed |  | - | n/a | |
| testSeqGen | rep2 | 290602668 | completed |  | - | n/a | |
| testSeqGen | rep3 | 933393725 | completed |  | - | n/a | |
| testSeqGen | rep4 | 88938131 | completed |  | - | n/a | |
| testSimulatedAlignment | rep1 | 231899804 | completed | 1 | 91 | 91 ⚠ | coalescent (test.231899804.log) |
| testSimulatedAlignment | rep2 | 642061937 | completed | 1 | 91 | 70 ⚠ | hky.kappa (test.642061937.log) |
| testSimulatedAlignment | rep3 | 298730249 | completed | 1 | 91 | 54 ⚠ | hky.kappa (test.298730249.log) |
| testSimulatedAlignment | rep4 | 70342620 | completed | 1 | 91 | 41 ⚠ | treeLikelihood (test.70342620.log) |

</details>
