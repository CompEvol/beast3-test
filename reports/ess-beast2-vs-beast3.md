# ESS: BEAST 2 vs BEAST 3 example runs

Generated 2026-11-17 14:37, tables updated 2026-11-17 16:30, with the `rep_status` / `rep_min_ess` functions of `scripts/run_report.py` (ESS as in `scripts/compare.py`, matching LogAnalyser), for the 12 example tests only.

## Setup

- beast2: `beast2/log/<test>/rep<N>/`, XMLs from `beast2/xml/` — BEAST.base 2.7.9, Java 25.0.2, run 2026-11-10 (re-runs 2026-11-17, see below)
- beast3: `beast3/log/<test>/rep<N>/`, XMLs from `beast3/xml/` — BEAST.base 2.8.0, Java 25.0.3, run 2026-11-17
- BEAST 3 app: BEAST v2.8.0 rc3; BEAST 2 app: "BEAST 2.7.7" launcher (BEAST.base 2.7.9)
- Replicates paired by number: beast2 rep N vs beast3 rep N. Seeds are listed but **not** required to match.
- ESS: minimum over all non-constant columns of all `*.log` files in a replicate, 10 % burn-in; ⚠ = below 200
- beast2 testTipDates rep1–rep4 were re-run on 2026-11-17 with chainLength 2,000,000 (doubled, as the 1,000,000 runs had min ESS < 200); rep1 and rep4 also with a new seed (seeds 505579092 and 894497562 still gave min ESS 69 and 181 at 2,000,000).
- Re-run on 2026-11-17 with the same seeds and longer chains, with `chainLength` and every logger's `logEvery` raised so the trace log has 2001 samples (1801 after burn-in), as the earlier runs had min ESS < 200: beast2 and beast3 testSimulatedAlignment (1,000,000 → 20,000,000, `logEvery` 10,000), beast2 testRandomLocalClock (2,000,000 → 100,000,000, `logEvery` 10,000 → 50,000), beast2 testRelaxedClock (1,000,000 → 10,000,000, `logEvery` 1,000 → 5,000), beast3 testUCLNclock (10,000,000 → 20,000,000, `logEvery` 1,000 → 10,000), beast3 testRandomLocalClock (2,000,000 → 100,000,000, `logEvery` 10,000 → 50,000), with rep1 on a new seed (seed 798545320 still gave min ESS 52 at 100,000,000, on `indicators.5`).
- Each version uses its own column names; the minimum may come from different columns in the two versions.

## Summary (minimum over replicates)

| Test | Type | Reps | beast2 completed | beast2 min ESS | beast2 lowest column | beast3 completed | beast3 min ESS | beast3 lowest column |
|---|---|---|---|---|---|---|---|---|
| testRandomLocalClock | MCMC | 4 | 4/4 | 357 | posterior in rep3 | 4/4 | 365 | indicators.7 in rep2 |
| testRelaxedClock | MCMC | 4 | 4/4 | 785 | posterior in rep2 | 4/4 | 596 | ucld.stdev in rep4 |
| testUCLNclock | MCMC | 4 | 4/4 | 321 | freqParameter.4 in rep1 | 4/4 | 637 | rate.variance in rep2 |
| testTipDates | MCMC | 4 | 4/4 | 271 | likelihood in rep2 | 4/4 | 353 | likelihood in rep1 |
| testTipDates2 | MCMC | 4 | 4/4 | 652 | freqParameter.2 in rep2 | 4/4 | 719 | freqParameter.1 in rep1 |
| testSRD06 | MCMC | 4 | 4/4 | 563 | thirdSites.hky.kappa in rep3 | 4/4 | 690 | thirdSites.freqParameter.1 in rep2 |
| testMultipleAlignments_randomTaxaOrder | MCMC | 4 | 4/4 | 651 | gammaShape in rep4 | 4/4 | 4877 | gammaShape in rep4 |
| testDirectSimulator | simulator | 4 | 4/4 | n/a |  | 4/4 | n/a |  |
| testDirectSimulator2 | simulator | 4 | 4/4 | 8564 | x in rep3 | 4/4 | 8589 | x in rep3 |
| testDirectSimulatorHierarchical | simulator | 4 | 4/4 | n/a |  | 4/4 | n/a |  |
| testSeqGen | simulator | 4 | 4/4 | n/a |  | 4/4 | n/a |  |
| testSimulatedAlignment | MCMC | 4 | 4/4 | 1384 | treeLikelihood in rep3 | 4/4 | 1205 | popSize in rep3 |

## Replicates (rep N vs rep N)

| Test | Rep | beast2 seed | beast2 status | beast2 samples | beast2 min ESS | beast2 column | beast3 seed | beast3 status | beast3 samples | beast3 min ESS | beast3 column | Same seed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| testRandomLocalClock | rep1 | 798545320 | completed | 1801 | 482 | posterior | 1010103437 | completed | 1801 | 743 | indicators.9 | no |
| testRandomLocalClock | rep2 | 337199670 | completed | 1801 | 547 | posterior | 337199670 | completed | 1801 | 365 | indicators.7 | yes |
| testRandomLocalClock | rep3 | 380329619 | completed | 1801 | 357 | posterior | 380329619 | completed | 1801 | 744 | indicators.9 | yes |
| testRandomLocalClock | rep4 | 562333788 | completed | 1801 | 471 | posterior | 562333788 | completed | 1801 | 389 | indicators.10 | yes |
| testRelaxedClock | rep1 | 317721114 | completed | 1801 | 864 | posterior | 317721114 | completed | 901 | 733 | rateCategories.1 | yes |
| testRelaxedClock | rep2 | 870681542 | completed | 1801 | 785 | posterior | 870681542 | completed | 901 | 599 | ucld.stdev | yes |
| testRelaxedClock | rep3 | 1025853318 | completed | 1801 | 812 | posterior | 1025853318 | completed | 901 | 633 | coalescent | yes |
| testRelaxedClock | rep4 | 913274257 | completed | 1801 | 852 | posterior | 913274257 | completed | 901 | 596 | ucld.stdev | yes |
| testUCLNclock | rep1 | 181696971 | completed | 9001 | 321 | freqParameter.4 | 181696971 | completed | 1801 | 994 | freqParameter.1 | yes |
| testUCLNclock | rep2 | 998153067 | completed | 9001 | 399 | freqParameter.1 | 998153067 | completed | 1801 | 637 | rate.variance | yes |
| testUCLNclock | rep3 | 1067999948 | completed | 9001 | 523 | freqParameter.1 | 1067999948 | completed | 1801 | 957 | freqParameter.2 | yes |
| testUCLNclock | rep4 | 887198521 | completed | 9001 | 404 | freqParameter.1 | 887198521 | completed | 1801 | 1012 | freqParameter.2 | yes |
| testTipDates | rep1 | 171681931 | completed | 1801 | 783 | likelihood | 505579092 | completed | 901 | 353 | likelihood | no |
| testTipDates | rep2 | 712860779 | completed | 1801 | 271 | likelihood | 712860779 | completed | 901 | 394 | likelihood | yes |
| testTipDates | rep3 | 766755024 | completed | 1801 | 392 | likelihood | 766755024 | completed | 901 | 393 | likelihood | yes |
| testTipDates | rep4 | 520154643 | completed | 1801 | 412 | tree.treeLength | 894497562 | completed | 901 | 393 | likelihood | no |
| testTipDates2 | rep1 | 204377550 | completed | 901 | 671 | freqParameter.1 | 204377550 | completed | 901 | 719 | freqParameter.1 | yes |
| testTipDates2 | rep2 | 618627302 | completed | 901 | 652 | freqParameter.2 | 618627302 | completed | 901 | 813 | freqParameter.3 | yes |
| testTipDates2 | rep3 | 547306038 | completed | 901 | 716 | freqParameter.3 | 547306038 | completed | 901 | 767 | freqParameter.4 | yes |
| testTipDates2 | rep4 | 351625106 | completed | 901 | 674 | freqParameter.2 | 351625106 | completed | 901 | 761 | tree.treeLength | yes |
| testSRD06 | rep1 | 629243466 | completed | 901 | 764 | firstAndSecondSites.freqParameter.2 | 629243466 | completed | 901 | 761 | firstAndSecondSites.freqParameter.4 | yes |
| testSRD06 | rep2 | 432746844 | completed | 901 | 688 | firstAndSecondSites.freqParameter.4 | 432746844 | completed | 901 | 690 | thirdSites.freqParameter.1 | yes |
| testSRD06 | rep3 | 542489439 | completed | 901 | 563 | thirdSites.hky.kappa | 542489439 | completed | 901 | 707 | thirdSites.freqParameter.1 | yes |
| testSRD06 | rep4 | 143610653 | completed | 901 | 710 | tree.height | 143610653 | completed | 901 | 712 | thirdSites.freqParameter.4 | yes |
| testMultipleAlignments_randomTaxaOrder | rep1 | 1016715609 | completed | 9001 | 689 | gammaShape | 1016715609 | completed | 9001 | 6107 | kappa | yes |
| testMultipleAlignments_randomTaxaOrder | rep2 | 38423589 | completed | 9001 | 898 | gammaShape | 38423589 | completed | 9001 | 6080 | gammaShape | yes |
| testMultipleAlignments_randomTaxaOrder | rep3 | 538607592 | completed | 9001 | 922 | gammaShape | 538607592 | completed | 9001 | 6574 | kappa | yes |
| testMultipleAlignments_randomTaxaOrder | rep4 | 119857108 | completed | 9001 | 651 | gammaShape | 119857108 | completed | 9001 | 4877 | gammaShape | yes |
| testDirectSimulator | rep1 | 783099780 | completed | - | n/a |  | 783099780 | completed | - | n/a |  | yes |
| testDirectSimulator | rep2 | 940416248 | completed | - | n/a |  | 940416248 | completed | - | n/a |  | yes |
| testDirectSimulator | rep3 | 323272233 | completed | - | n/a |  | 323272233 | completed | - | n/a |  | yes |
| testDirectSimulator | rep4 | 213944042 | completed | - | n/a |  | 213944042 | completed | - | n/a |  | yes |
| testDirectSimulator2 | rep1 | 73849810 | completed | 9000 | 9000 | x | 73849810 | completed | 9000 | 9000 | x | yes |
| testDirectSimulator2 | rep2 | 606844007 | completed | 9000 | 9000 | x | 606844007 | completed | 9000 | 9000 | x | yes |
| testDirectSimulator2 | rep3 | 436388536 | completed | 9000 | 8564 | x | 436388536 | completed | 9000 | 8589 | x | yes |
| testDirectSimulator2 | rep4 | 892665903 | completed | 9000 | 8940 | x | 892665903 | completed | 9000 | 8866 | x | yes |
| testDirectSimulatorHierarchical | rep1 | 715630407 | completed | - | n/a |  | 715630407 | completed | - | n/a |  | yes |
| testDirectSimulatorHierarchical | rep2 | 98674528 | completed | - | n/a |  | 98674528 | completed | - | n/a |  | yes |
| testDirectSimulatorHierarchical | rep3 | 102333413 | completed | - | n/a |  | 102333413 | completed | - | n/a |  | yes |
| testDirectSimulatorHierarchical | rep4 | 786067856 | completed | - | n/a |  | 786067856 | completed | - | n/a |  | yes |
| testSeqGen | rep1 | 55000162 | completed | - | n/a |  | 55000162 | completed | - | n/a |  | yes |
| testSeqGen | rep2 | 290602668 | completed | - | n/a |  | 290602668 | completed | - | n/a |  | yes |
| testSeqGen | rep3 | 933393725 | completed | - | n/a |  | 933393725 | completed | - | n/a |  | yes |
| testSeqGen | rep4 | 88938131 | completed | - | n/a |  | 88938131 | completed | - | n/a |  | yes |
| testSimulatedAlignment | rep1 | 231899804 | completed | 1801 | 1497 | treeLikelihood | 231899804 | completed | 1801 | 1268 | treeLikelihood | yes |
| testSimulatedAlignment | rep2 | 642061937 | completed | 1801 | 1749 | treeLikelihood | 642061937 | completed | 1801 | 1466 | popSize | yes |
| testSimulatedAlignment | rep3 | 298730249 | completed | 1801 | 1384 | treeLikelihood | 298730249 | completed | 1801 | 1205 | popSize | yes |
| testSimulatedAlignment | rep4 | 70342620 | completed | 1801 | 1634 | posterior | 70342620 | completed | 1801 | 1503 | hky.kappa | yes |
