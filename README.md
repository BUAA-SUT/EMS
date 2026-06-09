# EMS: Fine-grained Approach to Metamorphic Slicing for Fault Localization

This repository accompanies the paper:

> *Fine-grained approach to metamorphic slicing: Enhancing fault localization in the absence of oracle.*
> Daixu Ren, Zheng Zheng, Huai Liu, Tsong Yueh Chen.
> Submitted to *Information and Software Technology*.

It contains the source code, mutants, metamorphic relations (MRs), test cases, experimental scripts, and result spreadsheets needed to reproduce the empirical study in the paper.

---

## 1. Repository structure

```
EMS/
├── code/                      # Source code, mutants, MR implementations, scripts
│   ├── common/                # Shared modules
│   │   ├── publicFun.py       #   Core implementation: oms / ims / dms suspiciousness
│   │   ├── statisticResult.py #   Aggregates the per-program results into TOP-N tables
│   │   └── figure.py          #   Generates the figures in the paper from result xlsx
│   ├── TSQ/                   # 6  programs × 9  MRs  -- TriangleSquare
│   ├── DM/                    # 7  programs × 10 MRs  -- Determinant
│   ├── SMM/                   # 6  programs × 15 MRs  -- SparseMatrixMultiplication
│   ├── Tcas/                  # 20 programs × 9  MRs  -- Aircraft conflict detection
│   ├── PT/                    # 3  programs × 11 MRs  -- Print_tokens
│   ├── PT2/                   # 11 programs × 11 MRs  -- Print_tokens2
│   ├── PrimeCount/            # 17 programs × 3  MRs  -- Prime-counting function
│   ├── SeqMap/                # 4  programs × 3  MRs  -- Sequence mapping tool
│   └── grep/                  # 10 programs × 12 MRs  -- GNU grep
├── data/                      # Test pools, applicable test-case lists, result spreadsheets
│   ├── TSQ/ … grep/           # Per-program test inputs (where applicable)
│   └── results/               # All experimental result spreadsheets (.xlsx)
│       ├── result26..29_*.xlsx        # Raw per-program/per-mutant TOP-N results
│       │   (suffix: *_one = "only one failure-revealing test case in MR-violating MGs",
│       │            *_all = "all test cases in MR-violating MGs are failure-revealing",
│       │            *_nofs = "false-satisfaction MGs removed")
│       └── top-n*_26-29.xlsx          # Aggregated TOP-N tables used in the paper
└── docs/                      # Detailed reproduction notes, MR descriptions, mutant info
```

The 9 object programs together comprise 84 mutants and 83 MRs, matching Table 1 of the paper.

---

## 2. Quick start

The experiments are written in Python 3.8+ (with C/C++ object programs compiled via `gcc`/`g++`).
We recommend creating a virtual environment first:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

A minimal `requirements.txt` lists `numpy`, `coverage`, `openpyxl`, `matplotlib`, `pandas`, and `scipy`.

For the C/C++ subjects (`PT`, `PT2`, `grep`, `SeqMap`), build the per-mutant binaries from
source first — see [`docs/BUILD.md`](docs/BUILD.md) for the exact `gcc`/`g++` commands.

To re-run a single program (e.g., TSQ):

```bash
cd code/TSQ
python TSQ_test.py
```

The script will read the source test cases in `../../data/TSQ/`, run all mutants, compute coverage and metamorphic slicing under all weighting strategies, and write per-mutant fault-localization results to `../../data/results/`.

---

## 3. Reproducing the figures and tables in the paper

After every program has been executed, run:

```bash
cd code/common
python statisticResult.py     # Produces TOP-N aggregate tables (Tables 3-8)
python figure.py              # Produces Fig. 6 / Fig. 7 from result26..29 spreadsheets
```

Both scripts read from `data/results/` and write the output figures into `code/common/figures/` (created on first run).

The pre-computed result spreadsheets that back Tables 3–8 and Fig. 6 / Fig. 7 are already shipped under `data/results/`:

| Spreadsheet | Used in |
|-------------|---------|
| `result29_one.xlsx`, `result29_all.xlsx` | RQ1 (Fig. 6, Tables 3 & 4), RQ2 (Tables 6 & 7), RQ3 Part-II (Fig. 7) |
| `result29_nofs.xlsx` | RQ3 Part-I (Table 8) |
| `top-n-one_26-29.xlsx`, `top-n-all_26-29.xlsx`, `top-n_26-29.xlsx` | Aggregated TOP-N values used to fill the tables |

---

## 4. Random seeds and sampling strategy

All randomized steps use deterministic seeds so that experiments are bit-for-bit reproducible:

- TSQ / DM / SMM: source test cases are sampled with `random.seed(1)` (see `*_test.py`).
- Tcas / PT / PT2: source test cases come from the SIR `universe` test plans; no random sampling beyond shuffling for MG construction (`random.seed(1)`).
- PrimeCount / SeqMap: source inputs are generated according to the schemes in `genMR.py` / `coverage_*.py`.
- grep: 1 000 source test cases are sampled with `random.seed(1)` from the 171,634-test pool reused from prior studies (see `code/grep/test_grep.py`); the resulting per-MR applicable subset is documented in [`docs/grep_test_cases.md`](docs/grep_test_cases.md).

---

## 5. Mutants (faults)

The 84 mutants we used are stored under `code/<program>/Mutants/` (or `Mutant1.py`, `Mutant2.py`, ... for the small Python programs). For Tcas / PT / PT2 we use the SIR-released mutants together with author-generated ones; for the other programs we reuse the mutants from previously published MT studies, as detailed in:

- [`docs/mutants.md`](docs/mutants.md) — per-program mutant origin, mutation operator, and faulty line(s).

---

## 6. Metamorphic relations (MRs)

The 83 MRs (55 from prior studies + 28 newly defined by the authors) are described in:

- [`docs/MRs.md`](docs/MRs.md) — full natural-language description, source-test-case constraint, output relation, and reference for every MR.

For programs implemented in pure Python (TSQ / DM / SMM / Tcas), the MR logic is embedded in the `*_test.py` driver. For PT / PT2 it lives in `TestCase.py`. For PrimeCount / SeqMap / grep the MR class hierarchy is in `genMR.py` (or `MRs/MR.py` for grep).

---

## 7. Implementation of the weighting strategies

The three slicing strategies — original metamorphic slicing (`oms`), intersection emphasis strategy (`ims`), and symmetric difference emphasis strategy (`dms`) — are all implemented in `code/common/publicFun.py`:

- `MSlice_*` / `MSlice_one_*` / `MSlice_all_*` compute the suspiciousness vector under `oms`.
- `MSlice4_*` / `MSlice4_one_*` / `MSlice4_all_*` compute it under `ims` and `dms`, parameterised by the weight `ω ∈ [0.5, 0.98]` with step 0.02 (25 values per strategy × 30 risk formulas = 1 500 weight–formula combinations, as described in Section 4.3 of the paper).

The 30 risk formulas (Naish2, Wong3, GP13, Ochiai, Tarantula, …) are listed in Table 2 of the paper.
Refer to `code/common/publicFun.py` for the exact formula definitions used in the experiments.

---

## 8. Citing this work

If you use this code or data, please cite the paper above.

---

## 9. Contact

For questions about the artifact, please open a GitHub issue or contact the author Daixu Ren (<rendaixu@tiangong.edu.au>).
