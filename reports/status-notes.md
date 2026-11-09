<!-- Panels under the table on the status page (scripts/build_status_page.py).
     Each "## " heading starts a panel; "- " and "1. " lines become lists, other lines paragraphs.
     Inline `code` and **bold** are supported. -->

## Next steps

1. **Yao:** commit the trace logs, XMLs and beast.out for C05, C15, C17, C21, C24 (the trees are in Dropbox), and run C28.
1. **Sophie:** rerun C20 on rc2 (still rc1). Check C12's BEAST 3 XML for the gammaShape lower bound. Run the BEAST 2 side of C03 and C22 a little longer.
1. **Yuan:** let C04, C14, C16, C25, C29, C30 run to the end of the chain.
1. **After rc3:** run the existing C08 and C13 XMLs (C13 also needs a BEAST.base 2.7.9 refresh).

## Is rc3 needed first?

Only for C08 (calibrated Yule crash, fixed by beast3#198) and C13 (`SampleOffValues` Hastings ratio, beast3#203 and beast2#1223). Everything else can run on rc2 now.

rc3 also changes BEAUti 3's default priors (#208, e.g. Gamma → LogNormal(0, 8)). The matching BEAUti 2.7 change, BeastFX#111, is still open. Don't rebuild analyses in rc3 BEAUti until both versions have it.

## Known differences, not bugs

- **Gamma-shape `prior` offset** (C06, C18). BEAST 3 normalises the Exponential(1) prior on a shape bounded at 0.1, so the log prior is 0.1 higher per shape. The posterior is the same.
- **RLC indicators** (C14) are indexed by node number, which isn't tied to a clade, so they are compared by clade from the trees instead.
- **C27 calibration densities** are logged differently. Both versions match the analytic calibrations, U(4, 6) and U(8, 10).
