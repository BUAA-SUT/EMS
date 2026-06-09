# Reproduction Guide

This document gives a concrete, end-to-end recipe for reproducing every result in the paper
from the spreadsheets and scripts shipped in this repository.

## 1. Environment

```bash
git clone https://github.com/BUAA-SUT/EMS.git
cd EMS
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Tested with Python 3.10 / 3.12 on macOS 14 (Sonoma) and Ubuntu 22.04. C/C++ subjects were
compiled with `gcc 13` / `g++ 13`.

For coverage tracing of the C/C++ subjects (`Tcas`, `PT`, `PT2`, `PrimeCount`, `SeqMap`,
`grep`) we use `gcov`. Make sure `gcc` was compiled with coverage support (default on
GNU/Linux, available via Xcode CommandLineTools on macOS).

## 2. Pre-computed results (fastest path)

The full set of fault-localization results that back the figures and tables of the paper
is already shipped under `data/results/`.

To regenerate the figures (Fig. 6 and Fig. 7) and the TOP-N summary tables (Tables 3-7,
Table 8 of the paper):

```bash
cd code/common
mkdir -p figures
python figure.py            # writes Fig. 6 / 7 to ./figures/
python statisticResult.py   # prints TOP-N tables to stdout / writes top-n*.xlsx
```

The result spreadsheets are organised as follows:

| File pattern | Meaning |
|---|---|
| `result26..29_one.xlsx` | RQ1 / RQ2 / RQ3-Part-II runs under the **"only one failure-revealing test case in MR-violating MGs"** scenario |
| `result26..29_all.xlsx` | The same runs under the **"all test cases in MR-violating MGs are failure-revealing"** extreme scenario |
| `result26..29_nofs.xlsx` | The same runs after **removing false-satisfaction MGs** (RQ3 Part-I) |
| `top-n-one_26-29.xlsx`, `top-n-all_26-29.xlsx`, `top-n_26-29.xlsx` | Aggregated TOP-N tables across all 9 programs / 84 mutants |

## 3. Re-running the experiments from scratch

Each program has its own `*_test.py` driver under `code/<program>/`. Running the driver
will:

1. Load (or randomly generate) the source test cases from `data/<program>/`.
2. Build MGs by applying every applicable MR.
3. Execute every mutant against every test case and collect coverage / output information.
4. Compute the suspiciousness vector under `oms`, `ims` (25 weights), and `dms` (25 weights)
   for all 30 risk formulas.
5. Write the per-mutant TOP-N values into `data/results/result<N>_<scenario>.xlsx`.

Concrete commands:

```bash
cd code/TSQ        && python TSQ_test.py
cd ../DM           && python DM_test.py
cd ../SMM          && python SMM_test.py
cd ../Tcas         && python Tcas_test.py
cd ../PT           && python PT_test.py
cd ../PT2          && python PT2_test.py
cd ../PrimeCount   && python PC_test.py
cd ../SeqMap       && python SM_test.py
cd ../grep         && python test_grep.py
```

Wall-clock cost on a 2024 M-series laptop (single-threaded) is roughly:

| Program | Time |
|---|---|
| TSQ / DM / SMM | seconds each |
| Tcas | a few minutes |
| PT / PT2 | ~30 minutes each |
| PrimeCount / SeqMap | ~15 minutes each |
| grep | ~3 hours (dominated by mutant execution on 1,000 source test cases) |

After all runs finish, regenerate the aggregated tables and figures as in Section 2.

## 4. MR constraint filtering (especially for grep)

For `grep`, different MRs impose different structural constraints on the source pattern
(see `docs/grep_test_cases.md` for the full list). Not every test case is applicable to
every MR. Inside `test_grep.py`, the filtering is performed *before* MG construction:
each candidate source test case is checked against the MR's `is_applicable(t)` predicate;
only test cases passing the predicate are used to derive that MR's follow-up test cases.

For all other programs, every source test case is applicable to every MR — no filtering
is required.

## 5. Random seeds

All randomized routines (test-case sampling, MG construction shuffles, mutant ordering)
seed Python's `random` module with `random.seed(1)` (see the top of every `*_test.py`
script). With this seed, the experiments are bit-for-bit reproducible.

## 6. Statistical analysis

The Wilcoxon signed-rank tests with Bonferroni correction reported in Table 5 of the paper
can be reproduced via:

```bash
cd code/common
python -c "
import openpyxl, scipy.stats as ss
# load the top-n-one_26-29.xlsx workbook, extract per-formula TOP-N for each weight pair,
# and run wilcoxon(...). See statisticResult.py for the exact procedure.
"
```

The relevant aggregation logic lives in `statisticResult.py`; the function
`compare_strategies()` performs the paired comparison and applies Bonferroni correction
for the multiple (N value × weight pair) comparisons.
