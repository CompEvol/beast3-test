<!-- Panels under the table on the example-XML status page (scripts/build_status_page.py).
     Same format as reports/status-notes.md. -->

## Next steps

1. **Walter:** run and compare the 12 examples not run yet: the 8 converted MCMC examples (testRandomLocalClock, testRelaxedClock, testUCLNclock.json, testTipDates, testTipDates2, testSRD06, testMultipleAlignments_randomTaxaOrder, testSimulatedAlignment) and the 4 simulators (check that they run).
1. **Merge** [beast2#1227](https://github.com/CompEvol/beast2/pull/1227) (seqgen class names in testSeqGen and testSimulatedAlignment) and [beast2#1228](https://github.com/CompEvol/beast2/pull/1228) (testUCLNclock.json with explicit sequences). With them, every in-scope v2.7.8 example loads in BEAST 3.

Done since 10 Nov: testSliceHKY is excluded (`SliceOperator` was removed on purpose; in the CHANGELOG, beast3#236); the LogNormal(0, 8) kappa prior is merged (beast3#220).

## Backward compatibility

Every v2.7.8 example XML, unmodified, was loaded in BEAST 3. On 9 Nov **9 of 44** loaded. Since then:

- `TreeHeightLogger` (31 examples) is back as a deprecated class (beast3#235, merged);
- testSliceHKY is excluded, so the target is **43**;
- testSeqGen, testSimulatedAlignment and testUCLNclock.json load with the fixed copies in beast2#1227 and beast2#1228 (open).

With those, BEAST 3 loads all 43 (checked 10 Nov). The ones that load and run MCMC give the same posterior as BEAST 2.7.9.

## Known differences, not bugs

- **GTR-family `prior` offset** (testGTR, testRNA, testRestrictedGTR, testSYM, testTIM, testTN93, testTVM). A constant log 1e6 in `prior`; every model parameter matches.
- **Excluded:** testStarBeast and testStarBeastFBD are *BEAST 1 examples; that code was not migrated to BEAST 3.
