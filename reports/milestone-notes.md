<!-- Panels under the tables on the milestone page (scripts/build_status_page.py).
     Same format as reports/status-notes.md. -->

## To decide at the meeting

1. **Open pull requests:** only [#274](https://github.com/CompEvol/beast3/pull/274) is left; Walter reviewed it and the two problems he found are fixed. #254, #276, #278, #279 and #280 are merged.
1. **Branch protection.** The rule for `beast-base` ([#263](https://github.com/CompEvol/beast3/pull/263)) is merged. CODEOWNERS enforces nothing until an admin switches on branch protection for master.
1. **Bundled packages** (#248): bModelTest, ORC, SA, StarBeast3, CCD. Who builds and releases each against rc3 (Remco: bModelTest, StarBeast3; Jordan: ORC; SA; CCD)? Bundle MM too, for SA's `brachiopods.xml`?
1. **XML that changes** (#49, #38, #226): each is easier before the release than after it.
1. **Linux and Windows are untested.** CI builds the bundles (`release-bundles.yml`), but every tester uses a Mac, so no BEAUti or BEAST run in either round was on Linux or Windows. Who tests them before 2.8.0, on which machines, and how much (install, first-launch seeding of the bundled packages, a few BEAUti combinations)?
1. **The issues under "Decide"**: 2.8.0, 2.9.0 or close.

## Found on 12 Nov

- **Sixteen test classes were never run.** The tests of `beast.base.spec.type` and `beast.base.spec.domain` used JUnit 4 annotations, and the build has no JUnit 4 engine, so Maven found no tests in them and CI was green. [#270](https://github.com/CompEvol/beast3/pull/270), now merged, converts them: 77 tests now run, and all pass.
- **The slow tests that CI skips** (74 in beast-base) were run on master on 12 Nov: all pass except `TreePriorTest.testBSP`, which [#273](https://github.com/CompEvol/beast3/pull/273), merged, fixes.
- **`BeautiPriorValidationTest` failed in full local beast-fx runs**: an earlier test left a prior expanded through a static set. Fixed in [#279](https://github.com/CompEvol/beast3/pull/279), merged; it now also resets before each test class.
- **Messages for a value that is not valid now say why** ([#254](https://github.com/CompEvol/beast3/pull/254), merged): the element and the allowed range, or for a simplex the sum, instead of the domain's class name. A BSP file with wrong group sizes now gives "The values must sum to 5, but they sum to 6." BEAUti still builds its own message, so a simplex with a wrong sum shows a range there: [#281](https://github.com/CompEvol/beast3/issues/281), after #274.
- **`TreePriorTest.testBSP` fails on master, as it has since January**, on `skyline.groupSize.3` (CI skips the test). The expected values come from a single BEAST 1 run of 2011, never repeated; the group sizes were commented out in 2011 because BEAST 2 already disagreed, and switched back on in 2021. On 12 Nov, 4 seeds × 20M steps each: BEAST X 10.5.0 3.282 ± 0.013, BEAST 3 3.311 ± 0.012, BEAST 3 with the legacy BEAST 2 XML 3.289 ± 0.008, against 3.181 in the 2011 reference. BEAST X and BEAST 3 agree on all five group sizes (largest z 1.7); **the 2011 reference is the odd one out.** [#273](https://github.com/CompEvol/beast3/pull/273) replaces the five values with the BEAST X ones; the test then passes.

## Outside this repository

- [substmodels#8](https://github.com/BEAST2-Dev/substmodels/issues/8): every SSM model with rates crashes at the first posterior calculation, in 2.8.0-rc1 and in master. SSM is no longer to be bundled (#248).
- [starbeast3#19](https://github.com/rbouckaert/starbeast3/issues/19): StarBeast3 does not start with `mvn exec:exec` from its own project. It works as an installed package.
- **Package check** ([report](https://github.com/CompEvol/beast3-test/blob/main/reports/packages-check.md)): master against 2.8.0-rc1 shows no regressions in ORC, SA, MM, SSM, bModelTest and StarBeast3. A StarBeast3 parameter that was borderline with 8 replicates (z = 3.2) matches with 16 (z = 1.9); see the [notes](https://github.com/CompEvol/beast3-test/blob/main/reports/packages-notes.md).
- The released package zips that users install have not been tested, only the default branches built from source.

## How to read this page

- The lists are a snapshot of GitHub, taken at the time shown at the top. Refresh with `scripts/fetch_milestone.py` and commit.
- The groups and notes are **a suggestion for the meeting**, written by hand in `reports/milestone-triage.tsv`. They are not decisions.
- An issue new on the milestone since the last edit of that file shows as "Not sorted".
