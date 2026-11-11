<!-- Panels under the tables on the milestone page (scripts/build_status_page.py).
     Same format as reports/status-notes.md. -->

## To decide at the meeting

1. **Reviewers** for the three small pull requests: [#267](https://github.com/CompEvol/beast3/pull/267), [#268](https://github.com/CompEvol/beast3/pull/268) and [#270](https://github.com/CompEvol/beast3/pull/270). None has an approving review.
1. **Branch protection.** The rule for `beast-base` ([#263](https://github.com/CompEvol/beast3/pull/263)) is merged. CODEOWNERS enforces nothing until an admin switches on branch protection for master.
1. **Bundled packages** (#248): what to do about SSM.
1. **XML that changes** (#49, #38, #226): each is easier before the release than after it.
1. **Linux and Windows builds** (#81): who writes them, and by when.
1. **The issues under "Decide"**: 2.8.0, 2.9.0 or close.

## Found on 12 Nov

- **Sixteen test classes were never run.** The tests of `beast.base.spec.type` and `beast.base.spec.domain` used JUnit 4 annotations, and the build has no JUnit 4 engine, so Maven found no tests in them and CI was green. [#270](https://github.com/CompEvol/beast3/pull/270) converts them: 77 tests now run, and all pass.
- **`TreePriorTest.testBSP` fails on master.** It is tagged slow, so CI does not run it. `skyline.groupSize.3` has mean 3.350 against the expected 3.181 from BEAST 1, tolerance 0.148. One seed, so it may be chance; it has not been looked at, and there is no issue for it yet.

## Outside this repository

- [substmodels#8](https://github.com/BEAST2-Dev/substmodels/issues/8): every SSM model with rates crashes at the first posterior calculation, in 2.8.0-rc1 and in master. Blocks bundling SSM (#248).
- [starbeast3#19](https://github.com/rbouckaert/starbeast3/issues/19): StarBeast3 does not start with `mvn exec:exec` from its own project. It works as an installed package.
- **Package check** ([report](https://github.com/CompEvol/beast3-test/blob/main/reports/packages-check.md)): master against 2.8.0-rc1 shows no regressions in ORC, SA, MM, SSM, bModelTest and StarBeast3. One StarBeast3 parameter of 60 is borderline (z = 3.2) and not explained; see the [notes](https://github.com/CompEvol/beast3-test/blob/main/reports/packages-notes.md).
- The released package zips that users install have not been tested, only the default branches built from source.

## How to read this page

- The lists are a snapshot of GitHub, taken at the time shown at the top. Refresh with `scripts/fetch_milestone.py` and commit.
- The groups and notes are **a suggestion for the meeting**, written by hand in `reports/milestone-triage.tsv`. They are not decisions.
- An issue new on the milestone since the last edit of that file shows as "Not sorted".
