# BEAST 3 example runs

Generated 2026-11-17 13:21 by `scripts/run_examples.sh beast3`.

## Failed runs

None — every replicate completed.

## Setup

- Launcher: `/Applications/BEAST 2.8.0/bin/beast` (`-version`: BEAST v2.8.0 rc3, bModelTest v1.4.0, starbeast3 v1.3.1, CCD v1.2.2, SA v2.3.0, BEAST.base v2.8.0, BEAST.app v2.8.0, ORC v1.3.1)
- BEAST options: `-working -beagle_SSE -seed <seed>`
- Bundled package (seeded into the package dir): `BEAST.app.package.v2.8.0-SNAPSHOT.zip`, dated 2026-11-16 14:41
- Bundled package (seeded into the package dir): `BEAST.base.package.v2.8.0-SNAPSHOT.zip`, dated 2026-11-16 14:41
- Bundled package (seeded into the package dir): `BMT.v1.4.0.zip`, dated 2026-11-16 14:41
- Bundled package (seeded into the package dir): `CCD.v1.2.2.zip`, dated 2026-11-16 14:41
- Bundled package (seeded into the package dir): `ORC.v1.3.1.zip`, dated 2026-11-16 14:41
- Bundled package (seeded into the package dir): `SA.v2.3.0.zip`, dated 2026-11-16 14:41
- Bundled package (seeded into the package dir): `starbeast3.v1.3.1.zip`, dated 2026-11-16 14:41
- XMLs: copied by `scripts/copy_examples.sh` into `beast3/xml/` from the examples of `../beast3` (branch `master`, commit 0dbce1a)
- Java: 25.0.3
- Run date: 2026-11-17
- Machine: Darwin 25.6.0 (arm64)
- Replicates: 4 per example, seed per replicate in `beast.out`, the same as the other version's rep when that ran first
- ESS: minimum over all non-constant columns of all `*.log` files in a replicate, 10 % burn-in; ⚠ = below 200

## Summary

| Example | Source | Type | Completed | Min ESS | Lowest column |
|---|---|---|---|---|---|
| testRandomLocalClock | `beast3/xml/testRandomLocalClock.xml` | MCMC | 4/4 | 73 ⚠ | indicators.5 in rep4 |
| testRelaxedClock | `beast3/xml/testRelaxedClock.xml` | MCMC | 4/4 | 596 | ucld.stdev in rep4 |
| testUCLNclock | `beast3/xml/testUCLNclock.json` | MCMC | 4/4 | 159 ⚠ | rate.mean in rep3 |
| testTipDates | `beast3/xml/testTipDates.xml` | MCMC | 4/4 | 353 | likelihood in rep1 |
| testTipDates2 | `beast3/xml/testTipDates2.xml` | MCMC | 4/4 | 719 | freqParameter.1 in rep1 |
| testSRD06 | `beast3/xml/testSRD06.xml` | MCMC | 4/4 | 690 | thirdSites.freqParameter.1 in rep2 |
| testMultipleAlignments_randomTaxaOrder | `beast3/xml/testMultipleAlignments_randomTaxaOrder.xml` | MCMC | 4/4 | 4877 | gammaShape in rep4 |
| testDirectSimulator | `beast3/xml/testDirectSimulator.xml` | simulator | 4/4 | n/a |  |
| testDirectSimulator2 | `beast3/xml/testDirectSimulator2.xml` | simulator | 4/4 | 8589 | x in rep3 |
| testDirectSimulatorHierarchical | `beast3/xml/testDirectSimulatorHierarchical.xml` | simulator | 4/4 | n/a |  |
| testSeqGen | `beast3/xml/testSeqGen.xml` | simulator | 4/4 | n/a |  |
| testSimulatedAlignment | `beast3/xml/testSimulatedAlignment.xml` | MCMC | 4/4 | 26 ⚠ | coalescent in rep2 |

## Replicates

| Example | Rep | Seed | Status | Run time (s) | Samples | Min ESS | Column (file) |
|---|---|---|---|---|---|---|---|
| testRandomLocalClock | rep1 | 798545320 | completed | 4 | 181 | 89 ⚠ | indicators.6 (test.798545320.log) |
| testRandomLocalClock | rep2 | 337199670 | completed | 4 | 181 | 78 ⚠ | indicators.6 (test.337199670.log) |
| testRandomLocalClock | rep3 | 380329619 | completed | 4 | 181 | 82 ⚠ | indicators.10 (test.380329619.log) |
| testRandomLocalClock | rep4 | 562333788 | completed | 4 | 181 | 73 ⚠ | indicators.5 (test.562333788.log) |
| testRelaxedClock | rep1 | 317721114 | completed | 2 | 901 | 733 | rateCategories.1 (test.317721114.log) |
| testRelaxedClock | rep2 | 870681542 | completed | 2 | 901 | 599 | ucld.stdev (test.870681542.log) |
| testRelaxedClock | rep3 | 1025853318 | completed | 2 | 901 | 633 | coalescent (test.1025853318.log) |
| testRelaxedClock | rep4 | 913274257 | completed | 2 | 901 | 596 | ucld.stdev (test.913274257.log) |
| testUCLNclock | rep1 | 181696971 | completed | 47 | 9001 | 670 | freqParameter.2 (dna.log) |
| testUCLNclock | rep2 | 998153067 | completed | 50 | 9001 | 625 | freqParameter.1 (dna.log) |
| testUCLNclock | rep3 | 1067999948 | completed | 51 | 9001 | 159 ⚠ | rate.mean (dna.log) |
| testUCLNclock | rep4 | 887198521 | completed | 49 | 9001 | 548 | freqParameter.2 (dna.log) |
| testTipDates | rep1 | 505579092 | completed | 5 | 901 | 353 | likelihood (test.505579092.log) |
| testTipDates | rep2 | 712860779 | completed | 5 | 901 | 394 | likelihood (test.712860779.log) |
| testTipDates | rep3 | 766755024 | completed | 5 | 901 | 393 | likelihood (test.766755024.log) |
| testTipDates | rep4 | 894497562 | completed | 5 | 901 | 393 | likelihood (test.894497562.log) |
| testTipDates2 | rep1 | 204377550 | completed | 67 | 901 | 719 | freqParameter.1 (beast_204377550.log) |
| testTipDates2 | rep2 | 618627302 | completed | 67 | 901 | 813 | freqParameter.3 (beast_618627302.log) |
| testTipDates2 | rep3 | 547306038 | completed | 67 | 901 | 767 | freqParameter.4 (beast_547306038.log) |
| testTipDates2 | rep4 | 351625106 | completed | 68 | 901 | 761 | tree.treeLength (beast_351625106.log) |
| testSRD06 | rep1 | 629243466 | completed | 81 | 901 | 761 | firstAndSecondSites.freqParameter.4 (beast_629243466.log) |
| testSRD06 | rep2 | 432746844 | completed | 81 | 901 | 690 | thirdSites.freqParameter.1 (beast_432746844.log) |
| testSRD06 | rep3 | 542489439 | completed | 81 | 901 | 707 | thirdSites.freqParameter.1 (beast_542489439.log) |
| testSRD06 | rep4 | 143610653 | completed | 81 | 901 | 712 | thirdSites.freqParameter.4 (beast_143610653.log) |
| testMultipleAlignments_randomTaxaOrder | rep1 | 1016715609 | completed | 502 | 9001 | 6107 | kappa (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testMultipleAlignments_randomTaxaOrder | rep2 | 38423589 | completed | 502 | 9001 | 6080 | gammaShape (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testMultipleAlignments_randomTaxaOrder | rep3 | 538607592 | completed | 496 | 9001 | 6574 | kappa (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testMultipleAlignments_randomTaxaOrder | rep4 | 119857108 | completed | 500 | 9001 | 4877 | gammaShape (testMultipleAlignments_randomTaxaOrder.xml.log) |
| testDirectSimulator | rep1 | 783099780 | completed |  | - | n/a | |
| testDirectSimulator | rep2 | 940416248 | completed |  | - | n/a | |
| testDirectSimulator | rep3 | 323272233 | completed |  | - | n/a | |
| testDirectSimulator | rep4 | 213944042 | completed |  | - | n/a | |
| testDirectSimulator2 | rep1 | 73849810 | completed |  | 9000 | 9000 | x (testDirectSimulator2.log) |
| testDirectSimulator2 | rep2 | 606844007 | completed |  | 9000 | 9000 | x (testDirectSimulator2.log) |
| testDirectSimulator2 | rep3 | 436388536 | completed |  | 9000 | 8589 | x (testDirectSimulator2.log) |
| testDirectSimulator2 | rep4 | 892665903 | completed |  | 9000 | 8866 | x (testDirectSimulator2.log) |
| testDirectSimulatorHierarchical | rep1 | 715630407 | completed |  | - | n/a | |
| testDirectSimulatorHierarchical | rep2 | 98674528 | completed |  | - | n/a | |
| testDirectSimulatorHierarchical | rep3 | 102333413 | completed |  | - | n/a | |
| testDirectSimulatorHierarchical | rep4 | 786067856 | completed |  | - | n/a | |
| testSeqGen | rep1 | 55000162 | completed |  | - | n/a | |
| testSeqGen | rep2 | 290602668 | completed |  | - | n/a | |
| testSeqGen | rep3 | 933393725 | completed |  | - | n/a | |
| testSeqGen | rep4 | 88938131 | completed |  | - | n/a | |
| testSimulatedAlignment | rep1 | 231899804 | completed | 2 | 91 | 65 ⚠ | treeLikelihood (test.231899804.log) |
| testSimulatedAlignment | rep2 | 642061937 | completed | 2 | 91 | 26 ⚠ | coalescent (test.642061937.log) |
| testSimulatedAlignment | rep3 | 298730249 | completed | 2 | 91 | 75 ⚠ | coalescent (test.298730249.log) |
| testSimulatedAlignment | rep4 | 70342620 | completed | 2 | 91 | 84 ⚠ | treeLikelihood (test.70342620.log) |
