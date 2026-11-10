<!-- Panels under the table on the status page (scripts/build_status_page.py).
     Each "## " heading starts a panel; "- " and "1. " lines become lists, other lines paragraphs.
     Inline `code` and **bold** are supported. -->

## Next steps

1. **Yao:** on rc3, rebuild C15's BEAST 3 side with NonNegativeUniform(0, 10) on the mean clock rate (beast3#224; BEAUti 2.7 can't add one) and every other prior set to match the 2.7.9 XML, then rerun both; rerun C21 with the same birth-rate prior in both versions.
1. **Sophie:** rebuild C12's BEAST 2 side with the default Gamma(0.01, 100) clock-rate prior (it has LogNormal(1, 1.25)) and rerun it to the end of the chain. Run the BEAST 2 side of C03 and C22 a little longer.
1. **Yuan:** put C14's 100M tree files in Dropbox.
1. **After rc3:** run the existing C08 and C13 XMLs (C13 also needs a BEAST.base 2.7.9 refresh).

## Is rc3 needed first?

For C08 (calibrated Yule crash, fixed by beast3#198), C13 (`SampleOffValues` Hastings ratio, beast3#203 and beast2#1223) and C15 (NonNegativeUniform, beast3#224). On rc3, also check that BEAUti 3 refuses a BEAUti 2.7 file with a clear message (C28, beast3#229). Everything else can run on rc2 now.

rc3 also changes BEAUti 3's default priors (#208, e.g. Gamma(0.01, 100) → LogNormal(0, 8)). The matching BEAUti 2.7 change, BeastFX#111, is still open, so an analysis rebuilt in rc3's BEAUti gets different defaults from its 2.7.9 side: set every prior by hand to match the 2.7.9 XML.

## Known differences, not bugs

- **Gamma-shape `prior` offset** (C06, C18). BEAST 3 normalises the Exponential(1) prior on a shape bounded at 0.1, so the log prior is 0.1 higher per shape. The posterior is the same.
- **RLC indicators** (C14) are indexed by node number, which isn't tied to a clade, so they are compared by clade from the trees instead.
- **C27 calibration densities** are logged differently. Both versions match the analytic calibrations, U(4, 6) and U(8, 10).
