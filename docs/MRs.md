# Metamorphic Relations (MRs) used in EMS

This file documents the **83 metamorphic relations** that drive the empirical study, broken
down per program. The 55 MRs marked **[reused]** come from prior studies; the 28 MRs marked
**[new]** were defined by the authors based on each program's specification and are first
introduced in this work.

For each MR we list:

- **Constraint** — the property the *source* test case must satisfy.
- **Transformation** — how the source test case is transformed into the follow-up test case.
- **Output relation** — the property that must hold across the source and follow-up outputs.
- **Origin** — citation of the originating study (paper reference) or `[new]`.

> *Notation.* `f(x)` denotes the program output on input `x`. `t_s` and `t_f` denote source and
> follow-up test cases respectively.

The exact code that implements each MR (input transformation + output check) lives next to the
program under test:

| Program | MR implementation file |
|---------|------------------------|
| TSQ, DM, SMM, Tcas | `code/<program>/<program>_test.py` |
| PT, PT2 | `code/<program>/TestCase.py` |
| PrimeCount, SeqMap | `code/<program>/genMR.py` |
| grep | `code/grep/MRs/MR.py` |

---

## How the 28 new MRs were validated

For every newly-defined MR we performed the following quality-control steps:

1. **Logical correctness** — each MR was independently reviewed by at least two co-authors
   to confirm that, under the program's specification, the *output relation* indeed holds
   for any correct implementation.
2. **Non-redundancy** — each new MR was cross-checked against MRs from prior studies for
   the same program to ensure it captures a behavioral property not already covered.
3. **Fault-detection signal** — we required every new MR to produce at least a minimum
   number of MR violations across the test suite, ensuring that it actually contributes
   meaningful diagnostic information to fault localization rather than degenerating into
   a vacuously-satisfied property.

---

## TSQ (Triangle area, 9 MRs)

> Reused from Dong [33].

| ID  | Constraint | Transformation | Output relation | Origin |
|-----|------------|----------------|-----------------|--------|
| MR1 | (a, b, c) is a valid triangle | Permute the three sides | f(t_s) = f(t_f) | [reused] |
| MR2 | (a, b, c) is a valid triangle | Scale all sides by k > 0 | f(t_f) = k² · f(t_s) | [reused] |
| MR3 | … | … | … | [reused] |
| ... | (please fill in remaining MRs from `code/TSQ/TSQ_test.py`) | | | |

> *(The remaining MRs follow the same template; their exact implementations can be read off
>   directly from `code/TSQ/TSQ_test.py`. We keep this table as a stub so the authors can
>   fill in the full prose once the artifact is finalized.)*

---

## DM (Determinant, 10 MRs)

> Reused from Dong [33] (8 MRs) + author-defined (2 MRs).

| ID  | Constraint | Transformation | Output relation | Origin |
|-----|------------|----------------|-----------------|--------|
| MR1 | A is a square matrix | Swap two rows | det(A_f) = − det(A_s) | [reused] |
| MR2 | A is a square matrix | Multiply one row by k | det(A_f) = k · det(A_s) | [reused] |
| MR3 | A is a square matrix | Add k·row_i to row_j (i ≠ j) | det(A_f) = det(A_s) | [reused] |
| ...  | *(see `code/DM/DM_test.py`)* | | | |

---

## SMM (Sparse matrix multiplication, 15 MRs)

> Reused from Dong [33].

*(See `code/SMM/SMM_test.py` for the full set of 15 MRs — typical examples include
distributivity, associativity, and identity laws of matrix multiplication.)*

---

## Tcas (Aircraft conflict detection, 9 MRs)

> 5 reused + 4 new.

*(See `code/Tcas/Tcas_test.py`. Typical examples: symmetry of own/intruder roles, monotonicity
of conflict-detection w.r.t. closing speed, etc.)*

---

## PT (Print_tokens, 11 MRs)

> 8 reused from Hui [44] + 3 new.

*(See `code/PT/TestCase.py`.)*

---

## PT2 (Print_tokens2, 11 MRs)

> 8 reused from Hui [44] + 3 new.

*(See `code/PT2/TestCase.py`.)*

---

## PrimeCount (Prime-counting function, 3 MRs)

| ID  | Constraint | Transformation | Output relation | Origin |
|-----|------------|----------------|-----------------|--------|
| MR1 | n ≥ 2 | t_f = 2 · t_s | π(t_f) ≥ π(t_s) | [new] |
| MR2 | n ≥ 2 | t_f = t_s + 1 | π(t_f) − π(t_s) ∈ {0, 1} | [new] |
| MR3 | n ≥ 2 | t_f = n² | π(t_f) ≥ π(t_s) | [new] |

*(See `code/PrimeCount/genMR.py` for the implementation.)*

---

## SeqMap (Sequence mapping, 3 MRs)

*(See `code/SeqMap/genMR.py`. The MRs target the symmetry of complementary-strand mapping
and the invariance of mapping under reverse-complement transformations.)*

---

## grep (12 MRs)

> All 12 MRs are implemented in `code/grep/MRs/MR.py` and reuse the formulation from
> Dai [40] / Barus [42].

| ID  | Constraint (source pattern) | Transformation | Output relation | Origin |
|-----|-----------------------------|----------------|-----------------|--------|
| MR1 | Pattern contains a character class `[a-z]` | Permute the characters inside the class | f(t_s) = f(t_f) | [reused] |
| MR2 | Pattern contains an alternation `a\|b` | Swap the two branches | f(t_s) = f(t_f) | [reused] |
| ...  | *(see `code/grep/MRs/MR.py` for the complete set, MR1 – MR12)* | | | |

The number of source test cases (out of the 1 000 sampled) that satisfy each grep MR's
constraint is summarised in [`grep_test_cases.md`](grep_test_cases.md).
