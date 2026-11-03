# Work assignments

How the beast2 → beast3 example testing and conversion is split across 6 testers.
See [README.md](README.md) for what each step means.

**Excluded:** the *BEAST 1 examples (`testStarBeast.xml`, `testStarBeastFBD.xml`) are excluded because the *BEAST 1 code was not migrated to BEAST 3.
That leaves 42 examples: 18 to test and 24 to convert and test.

Replace **P1–P6** with names in the [Team](#team) table below; nothing else needs editing.

## How the work is split

- **By theme**: each person owns one group of related models, so they learn one part of
  BEAST well and can do the matching BEAUti and model-coverage work for it.
- **Balanced by effort**: an example that is already converted only needs testing (steps 1–5,
  about 1 unit of effort). An unconverted one also needs converting first (about 3 units). A
  simulator with no MCMC needs converting and a run check only (about 2 units). Each person has
  roughly 15 units, plus one shared group job.
- **Four eyes**: the model check (step 1) of each XML is reviewed by a partner, not by the
  person who converted or tested it. Partners: P1 ↔ P2, P3 ↔ P4, P5 ↔ P6.
- **Conversions go upstream**: a new BEAST 3 XML is submitted as a PR to
  [CompEvol/beast3](https://github.com/CompEvol/beast3) `beast-base/src/test/resources/beast.base/examples/`
  and a copy is added to `beast3/xml/` here.

## Team

| ID | Name | Theme | Group job | Reviewer of | Units |
|----|------|-------|-----------|-------------|:-----:|
| P1 | | Substitution models + Yule | — | P2 | 16 |
| P2 | | Data, partitions & alignments | — | P1 | 14 |
| P3 | | Calibrations | Owns `reports/model-coverage.md` | P4 | 15 |
| P4 | | Coalescent | NeSI setup: install BEAST 2 + 3, maintain `nesi/run.sl`, help with runs | P3 | 12 + setup |
| P5 | | Clocks & tip dates | Compiles the final `reports/REPORT.md` | P6 | 15 |
| P6 | | Simulators & multiple alignments | — | P5 | 14 |

## Per-person task list

| ID | Test only (already converted) | Convert, then test | BEAUti by hand (TODO 1) | Model coverage (TODO 2) |
|----|-------------------------------|--------------------|-------------------------|-------------------------|
| P1 | testGTR, testHKY.xml, testHKY.json, testJukesCantor, testRNA, testRestrictedGTR, testSYM, testTIM, testTN93, testTVM | testYuleCalibrated, testYuleUncalibrated | 2 analyses: different substitution models + gamma / invariant sites | Substitution model and site heterogeneity rows |
| P2 | bitflip, testJukesCantorShort, testJukesCantorShortUncertain, testJukesCantorShortUncertain2, testJukesCantorShortUncertain2MLE, testOpSubSchedule, testPlates, testYuleOneSite | testSRD06, testSliceHKY | 2 analyses: multiple partitions, linked/unlinked models, NEXUS + FASTA import | Partition and codon-position rows |
| P3 | — | testCalYule_5t_2c, testCalibration, testClassicRootCalibrationPrior, testConditionalRootCalibrationPrior, testTwoCalibrationsPrior | 2 analyses: taxon sets, MRCA priors, calibrated Yule | Calibration rows; builds the whole matrix |
| P4 | — | testBSP, testCoalescent, testEBSP, testExponentialGrowth | 2 analyses: constant / exponential coalescent, BSP | Coalescent tree prior rows |
| P5 | — | testRandomLocalClock, testRelaxedClock, testUCLNclock.json, testTipDates, testTipDates2 | 2 analyses: relaxed clocks with tip dates | Clock model and tip-date rows |
| P6 | — | testDirectSimulator, testDirectSimulator2, testDirectSimulatorHierarchical, testSeqGen, testSimulatedAlignment, testMultipleAlignments_randomTaxaOrder | 2 analyses: birth–death tree prior, multiple alignments with different taxa order | Birth–death rows |

## Example lookup

Look up any example to see who owns it. Owners update the **Status** column as they go.

Status: ⬜ not started · 🔄 converting · 🔍 model check · 🏃 running on NeSI · 📊 comparing · ✅ matched · ⚠️ borderline · ❌ not matched / blocked

| # | Example | Converted? | Task | Owner | Reviewer | Status | Issue / PR |
|---|---------|:----------:|------|:-----:|:--------:|:------:|------------|
| 1  | bitflip.xml | yes | test | P2 | P1 | ⬜ | |
| 2  | testBSP.xml | no | convert + test | P4 | P3 | ⬜ | |
| 3  | testCalYule_5t_2c.xml | no | convert + test | P3 | P4 | ⬜ | |
| 4  | testCalibration.xml | no | convert + test | P3 | P4 | ⬜ | |
| 5  | testClassicRootCalibrationPrior.xml | no | convert + test | P3 | P4 | ⬜ | |
| 6  | testCoalescent.xml | no | convert + test | P4 | P3 | ⬜ | |
| 7  | testConditionalRootCalibrationPrior.xml | no | convert + test | P3 | P4 | ⬜ | |
| 8  | testDirectSimulator.xml | no | convert + run check | P6 | P5 | ⬜ | |
| 9  | testDirectSimulator2.xml | no | convert + run check | P6 | P5 | ⬜ | |
| 10 | testDirectSimulatorHierarchical.xml | no | convert + run check | P6 | P5 | ⬜ | |
| 11 | testEBSP.xml | no | convert + test | P4 | P3 | ⬜ | |
| 12 | testExponentialGrowth.xml | no | convert + test | P4 | P3 | ⬜ | |
| 13 | testGTR.xml | yes | test | P1 | P2 | ⬜ | |
| 14 | testHKY.json | yes | test | P1 | P2 | ⬜ | |
| 15 | testHKY.xml | yes | test | P1 | P2 | ⬜ | |
| 16 | testJukesCantor.xml | yes | test | P1 | P2 | ⬜ | |
| 17 | testJukesCantorShort.xml | yes | test | P2 | P1 | ⬜ | |
| 18 | testJukesCantorShortUncertain.xml | yes | test | P2 | P1 | ⬜ | |
| 19 | testJukesCantorShortUncertain2.xml | yes | test | P2 | P1 | ⬜ | |
| 20 | testJukesCantorShortUncertain2MLE.xml | yes | test | P2 | P1 | ⬜ | |
| 21 | testMultipleAlignments_randomTaxaOrder.xml | no | convert + test | P6 | P5 | ⬜ | |
| 22 | testOpSubSchedule.xml | yes | test | P2 | P1 | ⬜ | |
| 23 | testPlates.xml | yes | test | P2 | P1 | ⬜ | |
| 24 | testRNA.xml | yes | test | P1 | P2 | ⬜ | |
| 25 | testRandomLocalClock.xml | no | convert + test | P5 | P6 | ⬜ | |
| 26 | testRelaxedClock.xml | no | convert + test | P5 | P6 | ⬜ | |
| 27 | testRestrictedGTR.xml | yes | test | P1 | P2 | ⬜ | |
| 28 | testSRD06.xml | no | convert + test | P2 | P1 | ⬜ | |
| 29 | testSYM.xml | yes | test | P1 | P2 | ⬜ | |
| 30 | testSeqGen.xml | no | convert + run check | P6 | P5 | ⬜ | |
| 31 | testSimulatedAlignment.xml | no | convert + test | P6 | P5 | ⬜ | |
| 32 | testSliceHKY.xml | no | convert + test | P2 | P1 | ⬜ | |
| 33 | testStarBeast.xml | excluded | — | — | — | — | *BEAST 1, code not migrated to BEAST 3 |
| 34 | testStarBeastFBD.xml | excluded | — | — | — | — | *BEAST 1, code not migrated to BEAST 3 |
| 35 | testTIM.xml | yes | test | P1 | P2 | ⬜ | |
| 36 | testTN93.xml | yes | test | P1 | P2 | ⬜ | |
| 37 | testTVM.xml | yes | test | P1 | P2 | ⬜ | |
| 38 | testTipDates.xml | no | convert + test | P5 | P6 | ⬜ | |
| 39 | testTipDates2.xml | no | convert + test | P5 | P6 | ⬜ | |
| 40 | testTwoCalibrationsPrior.xml | no | convert + test | P3 | P4 | ⬜ | |
| 41 | testUCLNclock.json | no | convert + test | P5 | P6 | ⬜ | |
| 42 | testYuleCalibrated.xml | no | convert + test | P1 | P2 | ⬜ | |
| 43 | testYuleOneSite.xml | yes | test | P2 | P1 | ⬜ | |
| 44 | testYuleUncalibrated.xml | no | convert + test | P1 | P2 | ⬜ | |

## Suggested timeline

| Week | Everyone | Group jobs |
|------|----------|------------|
| 1 | Read the README; install BEAST 2.7.8 and BEAST 3 locally; start the step 1 model checks of already-converted examples | P4 sets up NeSI installs and `nesi/run.sl`; P3 drafts the coverage matrix |
| 2–3 | Convert your unconverted examples, open beast3 PRs, partner reviews the model check | P3 shares the coverage gaps so everyone can plan new BEAUti XMLs |
| 4 | Submit NeSI runs (BEAST 2 + BEAST 3, ≥ 2 replicates); BEAUti-by-hand analyses | P4 helps with failed or slow jobs |
| 5 | Collect logs, compare posteriors, write up your section (template in README step 5) | P5 merges all sections into `reports/REPORT.md` |
| 6 | Rerun borderline examples with longer chains; follow up open issues | Coverage gap XMLs (TODO 2) as time allows |

## Notes

- If someone finishes early, take an example from the person with the most units left
  (P1), and update the Owner column.
- Re-check the beast3 examples folder before starting a conversion — someone upstream may
  already have done it.
