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
| TSQ | `code/TSQ/TSQ.py` |
| DM | `code/DM/DM.py` |
| SMM | `code/SMM/SMM.py` |
| Tcas | `code/Tcas/Tcas.py` |
| PT, PT2 | `code/<program>/PT.py` or `PT2.py` |
| PrimeCount, SeqMap | `code/<program>/genMR.py` |
| grep | `code/grep/MRs/MR.py` |

---

## How the new MRs were validated

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

> All 9 MRs reused from Dong [33] or Hui [44].

Input: triangle with sides `(a, b, c)`. Output: area `f(a, b, c)`.

| ID   | Constraint | Transformation | Output relation | Origin |
|------|------------|----------------|-----------------|--------|
| MR1  | Valid triangle `(a, b, c)` | Replace `a` with the median `a' = √(2b²+2c²−a²)`; keep `b`, `c` | f(a', b, c) = f(a, b, c) | [reused] |
| MR2  | Valid triangle `(a, b, c)` | Replace `b` with the median `b' = √(2a²+2c²−b²)`; keep `a`, `c` | f(a, b', c) = f(a, b, c) | [reused] |
| MR3  | Valid triangle `(a, b, c)` | Replace `c` with the median `c' = √(2a²+2b²−c²)`; keep `a`, `b` | f(a, b, c') = f(a, b, c) | [reused] |
| MR4  | Valid triangle `(a, b, c)` | Apply MR1, then apply MR2 to the result | f(t_f) = f(t_s) | [reused] |
| MR5  | Valid triangle `(a, b, c)` | Apply MR1, then apply MR3 to the result | f(t_f) = f(t_s) | [reused] |
| MR6  | Valid triangle `(a, b, c)` | Apply MR2, then apply MR1 to the result | f(t_f) = f(t_s) | [reused] |
| MR7  | Valid triangle `(a, b, c)` | Apply MR2, then apply MR3 to the result | f(t_f) = f(t_s) | [reused] |
| MR8  | Valid triangle `(a, b, c)` | Apply MR3, then apply MR1 to the result | f(t_f) = f(t_s) | [reused] |
| MR9  | Valid triangle `(a, b, c)` | Apply MR3, then apply MR2 to the result | f(t_f) = f(t_s) | [reused] |

---

## DM (Determinant, 10 MRs)

> MR1–MR4 reused from Dong [33]. MR5–MR10 are [new] — each composes two of the basic MRs.

Input: 3×3 matrix `A` (stored as a flat array). Output: det(A).

| ID   | Constraint | Transformation | Output relation | Origin |
|------|------------|----------------|-----------------|--------|
| MR1  | Any square matrix `A` | Swap two rows (rows 1 and 2) | det(A_f) = −det(A_s) | [reused] |
| MR2  | Any square matrix `A` | Subtract `k`·row₂ from row₁ (`k = 3`) | det(A_f) = det(A_s) | [reused] |
| MR3  | Any square matrix `A` | Transpose: A_f = A^T | det(A_f) = det(A_s) | [reused] |
| MR4  | det(A) ≠ 0 | Invert: A_f = A⁻¹ | det(A_f) = 1 / det(A_s) | [reused] |
| MR5  | Any square matrix `A` | Apply MR1 then MR2 | det(A_f) = −det(A_s) | [new] |
| MR6  | Any square matrix `A` | Apply MR2 then MR1 | det(A_f) = −det(A_s) | [new] |
| MR7  | Any square matrix `A` | Apply MR1 then MR3 | det(A_f) = −det(A_s) | [new] |
| MR8  | Any square matrix `A` | Apply MR3 then MR1 | det(A_f) = −det(A_s) | [new] |
| MR9  | Any square matrix `A` | Apply MR2 then MR3 | det(A_f) = det(A_s) | [new] |
| MR10 | Any square matrix `A` | Apply MR3 then MR2 | det(A_f) = det(A_s) | [new] |

---

## SMM (Sparse matrix multiplication, 15 MRs)

> MR1–MR9 reused from Dong [33]. MR10–MR15 are [new] — each composes two of the basic MRs.

Input: matrix pair `(A, B)`. Output: product `C = A·B`.

| ID   | Constraint | Transformation | Output relation | Origin |
|------|------------|----------------|-----------------|--------|
| MR1  | Matrices `(A, B)` with compatible dimensions | Transpose both: `(A_f, B_f) = (B^T, A^T)` | f(A_f, B_f) = f(A, B)^T | [reused] |
| MR2  | Matrices `(A, B)` | Left-multiply `A` by row-swap matrix `P`: `A_f = P·A`, `B_f = B` | f(A_f, B_f) = P·f(A, B) | [reused] |
| MR3  | Matrices `(A, B)` | Right-multiply `B` by row-swap matrix `P`: `A_f = A`, `B_f = B·P` | f(A_f, B_f) = f(A, B)·P | [reused] |
| MR4  | Matrices `(A, B)` | Left-multiply `A` by scalar matrix `Q(3)`: `A_f = Q(3)·A`, `B_f = B` | f(A_f, B_f) = Q(3)·f(A, B) | [reused] |
| MR5  | Matrices `(A, B)` | Right-multiply `B` by scalar matrix `Q(4)`: `A_f = A`, `B_f = B·Q(4)` | f(A_f, B_f) = f(A, B)·Q(4) | [reused] |
| MR6  | Matrices `(A, B)` | Scale `A` by scalar 6: `A_f = 6·A`, `B_f = B` | f(A_f, B_f) = 6·f(A, B) | [reused] |
| MR7  | Matrices `(A, B)` | Scale `B` by scalar 7: `A_f = A`, `B_f = 7·B` | f(A_f, B_f) = 7·f(A, B) | [reused] |
| MR8  | Matrices `(A, B)` | Add identity to `A`: `A_f = A + I`, `B_f = B` | f(A_f, B_f) = f(A, B) + B | [reused] |
| MR9  | Matrices `(A, B)` | Add identity to `B`: `A_f = A`, `B_f = B + I` | f(A_f, B_f) = A + f(A, B) | [reused] |
| MR10 | Matrices `(A, B)` | Apply MR1 then MR2 | f(t_f) satisfies combined relation | [new] |
| MR11 | Matrices `(A, B)` | Apply MR1 then MR3 | f(t_f) satisfies combined relation | [new] |
| MR12 | Matrices `(A, B)` | Apply MR2 then MR1 | f(t_f) satisfies combined relation | [new] |
| MR13 | Matrices `(A, B)` | Apply MR2 then MR3 | f(t_f) satisfies combined relation | [new] |
| MR14 | Matrices `(A, B)` | Apply MR3 then MR1 | f(t_f) satisfies combined relation | [new] |
| MR15 | Matrices `(A, B)` | Apply MR3 then MR2 | f(t_f) satisfies combined relation | [new] |

---

## Tcas (Aircraft conflict detection, 9 MRs)

> All 9 MRs reused from Hui [44].
>

Input: 12-element vector `(Cur_Vertical_Sep, High_Confidence, Two_of_Three_Reports_Valid,
Own_Tracked_Alt, Own_Tracked_Alt_Rate, Other_Tracked_Alt, Alt_Layer_Value,
Up_Separation, Down_Separation, Other_RAC, Other_Capability, Climb_Inhibit)`.
Output: advisory ∈ {UPWARD_RA, DOWNWARD_RA, UNRESOLVED}.

| ID  | Transformation summary | Output relation | Origin |
|-----|------------------------|-----------------|--------|
| MR1 | Adjust own/intruder altitudes to equalise their relative position w.r.t. the midpoint, preserving advisory direction | f(t_f) = f(t_s) | [reused] |
| MR2 | Adjust Up/Down separation to reinforce the current advisory direction | f(t_f) = f(t_s) | [reused] |
| MR3 | Increment or decrement `Alt_Layer_Value` consistent with current advisory | f(t_f) = f(t_s) | [reused] |
| MR4 | Apply MR1 then MR2 | f(t_f) = f(t_s) | [reused] |
| MR5 | Apply MR1 then MR3 | f(t_f) = f(t_s) | [reused] |
| MR6 | Apply MR2 then MR1 | f(t_f) = f(t_s) | [reused] |
| MR7 | Apply MR3 then MR1 | f(t_f) = f(t_s) | [reused] |
| MR8 | Apply MR2 then MR3 | f(t_f) = f(t_s) | [reused] |
| MR9 | Apply MR3 then MR2 | f(t_f) = f(t_s) | [reused] |

---

## PT (Print_tokens, 11 MRs)

> MR1–MR3 reused from Hui [44]. MR4–MR9 are [new] (compositions). MR10–MR11 are [new]
> (standalone).
>

Input: source-code token stream (file). Output: token-type count vector.

| ID   | Transformation | Output relation | Origin |
|------|----------------|-----------------|--------|
| MR1  | Randomly swap case of ~50% of lines | f(t_f) = f(t_s) | [reused] |
| MR2  | Truncate each line at its first `;` (drop the trailing comment) | f(t_f) = f(t_s) | [reused] |
| MR3  | Prepend `;` to ~50% of lines (comment them out) | f(t_f)[i] ≤ f(t_s)[i] for all token types i | [reused] |
| MR4  | Apply MR1 then MR2 | f(t_f) = f(t_s) | [new] |
| MR5  | Apply MR2 then MR1 | f(t_f) = f(t_s) | [new] |
| MR6  | Apply MR1 then MR3 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR7  | Apply MR3 then MR1 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR8  | Apply MR2 then MR3 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR9  | Apply MR3 then MR2 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR10 | Duplicate ~10% of lines (append copies at end) | f(t_f)[i] ≥ f(t_s)[i] for all i | [new] |
| MR11 | Remove ~10% of lines | f(t_f)[i] ≤ f(t_s)[i] for all i | [new] |

---

## PT2 (Print_tokens2, 11 MRs)

> Identical MR set to PT (same `PT2.py` implementation mirrors `PT.py`).
>
> ⚠️ Same confirmation needed as PT above.

| ID   | Transformation | Output relation | Origin |
|------|----------------|-----------------|--------|
| MR1  | Randomly swap case of ~50% of lines | f(t_f) = f(t_s) | [reused] |
| MR2  | Truncate each line at its first `;` | f(t_f) = f(t_s) | [reused] |
| MR3  | Prepend `;` to ~50% of lines | f(t_f)[i] ≤ f(t_s)[i] | [reused] |
| MR4  | Apply MR1 then MR2 | f(t_f) = f(t_s) | [new] |
| MR5  | Apply MR2 then MR1 | f(t_f) = f(t_s) | [new] |
| MR6  | Apply MR1 then MR3 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR7  | Apply MR3 then MR1 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR8  | Apply MR2 then MR3 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR9  | Apply MR3 then MR2 | f(t_f)[i] ≤ f(t_s)[i] | [new] |
| MR10 | Duplicate ~10% of lines | f(t_f)[i] ≥ f(t_s)[i] | [new] |
| MR11 | Remove ~10% of lines | f(t_f)[i] ≤ f(t_s)[i] | [new] |

---

## PrimeCount (Prime-counting function, 3 MRs)

> All 3 MRs reused.

Input: integer `n ≥ 2`. Output: π(n) = number of primes ≤ n.

| ID  | Constraint | Transformation | Output relation | Origin |
|-----|------------|----------------|-----------------|--------|
| MR1 | n ≥ 2 | t_f = t_s + k, k ~ Uniform(1, 99) | π(t_f) ≥ π(t_s) | [reused] |
| MR2 | n ≥ 2 | t_f = t_s + 1 | π(t_f) − π(t_s) ∈ {0, 1} | [reused] |
| MR3 | n ≥ 2 | t_f = t_s + y, y ~ Uniform(1, t_s); also generate follow t_f₂ = y | π(t_f) ≥ π(t_s) and π(t_f) ≥ π(y) | [reused] |

*(See `code/PrimeCount/genMR.py` for the implementation.)*

---

## SeqMap (Sequence mapping, 3 MRs)

> All 3 MRs reused.

Input: edit distance `e` (integer 0–4), target sequence `T` (list of strings), query sequence
`p` (string). Output: alignment map `M`.

| ID  | Constraint | Transformation | Output relation | Origin |
|-----|------------|----------------|-----------------|--------|
| MR1 | Any valid `(e, T, p)` | Randomly select a non-empty subset of sequences from `T` and append them to `p` | Output changes reflect the extended query | [reused] |
| MR2 | `e` ∉ {0, 4} | Randomly change `e` to a different value in [0, 4] | Mapping result changes accordingly with the new edit tolerance | [reused] |
| MR3 | `len(p) ≥ 4` | Randomly trim `p` from either the front or the back by 1 to `len(p)−1` characters | Trimmed query produces a subset of the original alignments | [reused] |

*(See `code/SeqMap/genMR.py` for the implementation.)*

---

## grep (12 MRs)

> All 12 MRs reused from Dai [40] / Barus [42].

Input: regex pattern (string). Output: set of matching lines from target file.

| ID   | Constraint | Transformation | Output relation | Origin |
|------|------------|----------------|-----------------|--------|
| MR1  | Pattern contains a range character class `[x-y]` | Randomly permute the characters inside the class | f(t_f) = f(t_s) | [reused] |
| MR2  | Pattern contains a range class `[x-y]` | Expand range to explicit alternation `x\|x+1\|…\|y` | f(t_f) = f(t_s) | [reused] |
| MR3  | Pattern contains a non-range character class `[xyz…]` | Expand each character to a singleton class `[x]\|[y]\|…` | f(t_f) = f(t_s) | [reused] |
| MR4  | Pattern contains a range class `[x-y]` | Split the range into two adjacent sub-ranges `[x-m]\|[m+1-y]` | f(t_f) = f(t_s) | [reused] |
| MR5  | Pattern is a set of individual characters | Reassemble as a character class `[…]` in random order | f(t_s) ⊆ f(t_f) | [reused] |
| MR6  | Pattern is a set of individual characters | Reassemble as an alternation `a\|b\|…` in random order | f(t_s) ⊆ f(t_f) | [reused] |
| MR7  | Pattern contains a range class `[x-y]` | Shrink range by removing its last character: `[x-(y−1)]` | f(t_f) ⊆ f(t_s) | [reused] |
| MR8  | Pattern contains a range class `[x-y]` | Extend range by one character: `[x-(y+1)]` | f(t_s) ⊆ f(t_f) | [reused] |
| MR9  | Any pattern | Append `\|[[:digit:]]` to the pattern | f(t_s) ⊆ f(t_f) | [reused] |
| MR10 | Pattern contains a normal literal | Append a quantifier (`{1}` or `+`) to the literal | f(t_f) = f(t_s) | [reused] |
| MR11 | Pattern contains `\w`, `\W`, `[[:alnum:]]`, or `[^[:alnum:]]` | Replace with its complement class | f(t_f) verified against word-count file | [reused] |
| MR12 | Pattern contains a normal literal | Replace each character of the literal with `.` (match-any) | f(t_s) ⊆ f(t_f) | [reused] |

The number of source test cases (out of the 1 000 sampled) that satisfy each grep MR's
constraint is summarised in [`grep_test_cases.md`](grep_test_cases.md).
