# Batch comparison (beast2 vs beast3, burn-in 10%)

| Name | Reps (beast2/beast3) | Min ESS | Max z | Max clade Δp | Flagged | Verdict |
|---|---|---:|---:|---:|---:|---|
| testBSP | 2/2 | 2429 | 1.911 | 0.018 | 0 | matched |
| testCalYule_5t_2c | 2/2 | 355 | 2.098 | 0.005 | 0 | matched |
| testCalYule_5t_2c-analytic | 4/4 | 4089 | 1.054 | 0.006 | 0 | matched |
| testCalibration | 2/2 | 571 | 1.328 | 0.000 | 0 | matched |
| testClassicRootCalibrationPrior | 2/2 | 3318 | 0.6507 | 0.009 | 0 | matched |
| testCoalescent | 2/2 | 1977 | 1.88 | 0.007 | 0 | matched |
| testConditionalRootCalibrationPrior | 2/2 | 9 | 4.859 | 0.083 | 2 | not matched (ESS < 200) |
| testConditionalRootCalibrationPrior-analytic | 2/2 | 9 | 4.859 | 0.083 | 2 | not matched (ESS < 200) |
| testEBSP | 2/2 | 475 | 2.657 | 0.010 | 0 | matched |
| testExponentialGrowth | 2/2 | 1898 | 1.058 | 0.010 | 0 | matched |
| testTwoCalibrationsPrior | 2/2 | 3725 | 1.625 | 0.004 | 0 | matched |
| testYuleCalibrated | 2/2 | 566 | 1.317 | 0.006 | 0 | matched |
| testYuleUncalibrated | 4/4 | 590 | 2.103 | 0.002 | 0 | matched |
