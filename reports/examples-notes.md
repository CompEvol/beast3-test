<!-- Panels under the table on the example-XML status page (scripts/build_status_page.py).
     Same format as reports/status-notes.md. -->

## Next steps

1. **Walter:** run and compare the 8 converted MCMC examples (testRandomLocalClock, testRelaxedClock, testUCLNclock.json, testTipDates, testTipDates2, testSRD06, testMultipleAlignments_randomTaxaOrder, testSimulatedAlignment), and check the 4 simulators run.
1. **Decide:** whether testSliceHKY is excluded or `SliceOperator` is ported.
1. **Merge:** [beast3#220](https://github.com/CompEvol/beast3/pull/220), which changes the kappa prior in testHKY, testHKY.json and testOpSubSchedule to LogNormal(0, 8).
1. **Decide:** whether the BEAST 2 names that stop old XMLs loading (below) come back as aliases, or go in the release notes.

## Backward compatibility

Every v2.7.8 example XML, unmodified, was loaded in BEAST 3 master on 9 Nov. **9 of 44 load.** The rest fail on:

- `TreeHeightLogger` (31 examples)
- the `beast.app.seqgen.*` classes (testSeqGen, testSimulatedAlignment)
- `SliceOperator` (testSliceHKY)
- the JSON sequence format (testUCLNclock.json)

The 6 that load and run MCMC give the same posterior as BEAST 2.7.9.

## Known differences, not bugs

- **GTR-family `prior` offset** (testGTR, testRNA, testRestrictedGTR, testSYM, testTIM, testTN93, testTVM). A constant log 1e6 in `prior`; every model parameter matches.
- **Excluded:** testStarBeast and testStarBeastFBD are *BEAST 1 examples; that code was not migrated to BEAST 3.
