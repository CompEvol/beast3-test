<!-- Panels under the table on the status page (scripts/build_status_page.py).
     Each "## " heading starts a panel; "- " and "1. " lines become lists, other lines paragraphs.
     Inline `code` and **bold** are supported. -->

## The rc2 round is finished (12 Nov)

24 of 30 combinations pass. The other six are carried into the [rc3 round](rc3.html), with what they still need:

- **C08 → R02** (Sophie): crashed on rc1 and rc2; fixed by beast3#198, so it runs on rc3.
- **C12 → R04** (Sophie): rebuild the BEAST 2 side with the same clock-rate prior as BEAST 3, and run to the end of the chain.
- **C13 → R05** (Eva): both versions had the `SampleOffValues` Hastings bug, fixed in beast3#203 and beast2#1223; needs rc3 and the matching BEAST.base 2.7.9 refresh.
- **C14 → R06** (Yuan): chains too short; Yuan's 100M tree files still to go in Dropbox.
- **C15 → R07** (Yao): set the BEAST 3 mean clock-rate prior to NonNegativeUniform(0, 10) (beast3#224) and every other prior to match the 2.7.9 XML.
- **C21 → R08** (Yao): the same birth-rate prior in both versions.

## Known differences, not bugs

- **Gamma-shape `prior` offset** (C06, C18). BEAST 3 normalises the Exponential(1) prior on a shape bounded at 0.1, so the log prior is 0.1 higher per shape. The posterior is the same.
- **RLC indicators** (C14) are indexed by node number, which isn't tied to a clade, so they are compared by clade from the trees instead.
- **C27 calibration densities** are logged differently. Both versions match the analytic calibrations, U(4, 6) and U(8, 10).
