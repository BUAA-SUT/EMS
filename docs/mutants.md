# Mutants (faulty versions) used in EMS

Across the 9 object programs we use **84 mutants** in total, matching column 5 of Table 1 of
the paper. The mutants come from two sources:

1. **SIR-released mutants** for `Tcas`, `PT`, and `PT2` (the Siemens Suite [35]).
2. **Author-collected mutants** reused from prior MT studies for the other six programs
   (Dong [33, 34], Dai [39], Barus [42]).

For the Siemens Suite, many of the SIR mutants could not produce any MR violation under the
designed MRs and were therefore filtered out. To keep the per-program mutant count comparable
across all subjects, we additionally generated some new mutants for `Tcas`, `PT`, and `PT2`
using standard mutation operators (arithmetic-operator-replacement, relational-operator-
replacement, constant-replacement, and boundary-value perturbation). Mutants that failed to
compile were eliminated.

The selected mutants per program are listed below.

| Program     | #Mutants | Mutant location                                  |
|-------------|----------|--------------------------------------------------|
| TSQ         | 6        | `code/TSQ/Mutant1.py … Mutant6.py`               |
| DM          | 7        | `code/DM/Mutant1.py … Mutant7.py`                |
| SMM         | 6        | `code/SMM/Mutant2.py … Mutant7.py` (Mutant1 not used) |
| Tcas        | 20       | `code/Tcas/Mutant1.py … Mutant20.py`             |
| PT          | 3        | `code/PT/Mutants/printtokens_v1, v2, v11`        |
| PT2         | 11       | `code/PT2/Mutants/printtokens2_v4 … v14`         |
| PrimeCount  | 17       | `code/PrimeCount/Mutants/PrimeCount_v1 … v17`    |
| SeqMap      | 4        | `code/SeqMap/Mutants/seqmap_v1 … v4` (v5 = duplicate of v4) |
| grep        | 10       | `code/grep/Mutants/grep_v1 … v11` (v3 excluded)                 |
| **Total**   | **84**   |                                                  |

> Note: each program directory includes a `_v0` (or equivalent) **non-faulty baseline**
> (e.g. `grep_v0`, `seqmap_v0`, `PrimeCount_v0`). These baselines are kept for sanity
> checking and are *not* counted as faulty mutants.

---

## TSQ (`code/TSQ/Mutant*.py`)

All 6 mutants are arithmetic-operator or operand mutations introduced into the area
computation of `Trisquare.trisquare()` in `Original.py`.

| Mutant  | Faulty line | Change | Affected branch |
|---------|-------------|--------|-----------------|
| Mutant1 | 21 | `pow(Min/2,2)` → `pow(mid/2,2)` | Acute isosceles (Max == mid): wrong divisor in altitude calculation |
| Mutant2 | 26 | `pow(Max/2,2)` → `pow(mid/2,2)` | Acute isosceles (Min == mid): wrong divisor in altitude calculation |
| Mutant3 | 29 | `(Max+mid+Min)/2` → `(Max+mid+Min)*2` | Irregular acute triangle: Heron's formula semi-perimeter multiplied instead of halved |
| Mutant4 | 34 | `mid*Min/2` → `mid*Min` | Right triangle: missing division by 2 in area formula |
| Mutant5 | 40 | `Max*h/2` → `Max*h` | Obtuse isosceles triangle: missing division by 2 in area formula |
| Mutant6 | 42 | `pow(Max,2)+pow(mid,2)-pow(Min,2)` → `pow(Max,2)+pow(Min,2)-pow(mid,2)` | Irregular obtuse triangle: swapped `mid` and `Min` operands in altitude base calculation |

---

## DM (`code/DM/Mutant*.py`)

All 7 mutants target `DeterMinant.Determinant()` and `DeterMinant.DeterComp()` in
`Original.py`. Mutants 1–5 affect the triangular-matrix fast paths; Mutants 6–7 affect
the general cofactor-expansion path.

| Mutant  | Faulty line | Change | Description |
|---------|-------------|--------|-------------|
| Mutant1 | 21 | `result *= A[i*n+i]` → `result += A[i*n+i]` | Upper/lower triangular branch: `*=` replaced by `+=` when computing diagonal product |
| Mutant2 | 24 | `math.pow(-1, n*(n-1)/2)` → `math.pow(1, n*(n-1)/2)` | Anti-diagonal branch: sign factor base changed from `-1` to `1`, flipping sign |
| Mutant3 | 21 | `A[i*n+i]` → `A[i*n]` | Upper/lower triangular branch: diagonal index `i*n+i` replaced by first-column index `i*n` |
| Mutant4 | 21 | `A[i*n+i]` → `A[i*n+1]` | Upper/lower triangular branch: diagonal index replaced by fixed column-1 index |
| Mutant5 | 27 | `result *= A[i*n+(n-1-i)]` → `result += A[i*n+(n-1-i)]` | Anti-diagonal branch: `*=` replaced by `+=` |
| Mutant6 | 42 | `mid += ... * math.pow(-1,2+i) * ...` → `mid *= ... * math.pow(1,2+i) * ...` | Cofactor expansion: `+=` → `*=` and base `-1` → `1` in sign factor |
| Mutant7 | 42 | `mid += ... * math.pow(-1,2+i) * ...` → `mid *= ... * math.pow(-1,2+i) * ...` | Cofactor expansion: `+=` replaced by `*=` (sign factor preserved) |

---

## SMM (`code/SMM/Mutant*.py`)

6 mutants are used (Mutant2–Mutant7); Mutant1 is present in the directory but excluded from
the experiment (it removes the `nz = nz + 1` increment, which was found to produce no usable
MR violation signal). All 7 files target the inner loop of `Smm.SparseMatMul()` in
`Original.py`.

| Mutant  | Faulty line | Change | Description |
|---------|-------------|--------|-------------|
| Mutant1 | 45 | `nz = nz + 1` removed | New non-zero entry path: counter increment deleted, overwriting subsequent entries |
| Mutant2 | 43 | `c[nz] = aij * b[k]` → `c[nz] = b[k]` | New entry path: `aij` factor dropped from product |
| Mutant3 | 43 | `c[nz] = aij * b[k]` → `c[nz] = aij` | New entry path: `b[k]` factor dropped from product |
| Mutant4 | 48 | `c[icol] + aij * b[k]` → `c[icol] + aij` | Accumulation path: `b[k]` factor dropped |
| Mutant5 | 47 | `c[icol] + aij * b[k]` → `c[icol] + b[k]` | Accumulation path: `aij` factor dropped |
| Mutant6 | 47 | `c[icol] + aij * b[k]` → `c[icol] + aij + b[k]` | Accumulation path: `*` replaced by `+` |
| Mutant7 | 50 | `mask[jc[k]] = -1` → `mask[jc[i]] = -1` | Mask-reset loop: loop variable `k` replaced by outer loop variable `i` |

---

## Tcas (`code/Tcas/Mutant*.py`)

20 mutants covering relational-operator-replacement (ROR), logical-operator-replacement
(LOR), arithmetic-operator-replacement (AOR), and operand-replacement (ORR) faults across
all major conditional branches of the TCAS advisory logic.

| Mutant   | Method / location | Change | Operator class |
|----------|-------------------|--------|----------------|
| Mutant1  | `Non_Crossing_Biased_Climb` line 19 | `Inhibit_Biased_Climb() > Down_Separation` → `< ` | ROR |
| Mutant2  | `Own_Above_Threat` line 16 | `Other_Tracked_Alt < Own_Tracked_Alt` → `>` | ROR |
| Mutant3  | `Tcas` line 59 | `High_Confidence and (Rate <= OLEV) and (Sep > MAXALTDIFF)` → first `and` → `or` | LOR |
| Mutant4  | `Tcas` line 63 | `if enabled and (…)` → `if enabled or (…)` | LOR |
| Mutant5  | `Inhibit_Biased_Climb` line 7 | `Up_Separation + NOZCROSS` → `+ MINSEP` | ORR |
| Mutant6  | `Tcas` line 61 | `Two_of_Three_Reports_Valid and Other_RAC == NO_INTENT` → `and` → `or` | LOR |
| Mutant7  | `Non_Crossing_Biased_Climb` line 24 | `(Cur_Vertical_Sep >= MINSEP) and (Up_Separation >= ALIM())` → `and` → `or` | LOR |
| Mutant8  | `Tcas` line 60 | `enabled = … and (Cur_Vertical_Sep > MAXALTDIFF)` — last conjunct deleted (missing code) | Code deletion |
| Mutant9  | `Inhibit_Biased_Climb` line 7 | `Up_Separation + NOZCROSS` → `- NOZCROSS` | AOR |
| Mutant10 | `Tcas` line 60 | `Other_Capability == TCAS_TA` → `!=` | ROR |
| Mutant11 | `Non_Crossing_Biased_Climb` line 22 | `Down_Separation >= ALIM()` → `<` | ROR |
| Mutant12 | `Non_Crossing_Biased_Descend` line 35 | `Up_Separation >= ALIM()` → `<` | ROR |
| Mutant13 | `Non_Crossing_Biased_Climb` line 19 | `Inhibit_Biased_Climb() > Down_Separation` → `<=` | ROR |
| Mutant14 | `Non_Crossing_Biased_Descend` line 29 | `Inhibit_Biased_Climb() > Down_Separation` → `<=` | ROR |
| Mutant15 | `Tcas` line 59 | `Cur_Vertical_Sep > MAXALTDIFF` → `<=` | ROR |
| Mutant16 | `Tcas` line 58 | `Own_Tracked_Alt_Rate <= OLEV` → `>` | ROR |
| Mutant17 | `Own_Below_Threat` line 13 | `Own_Tracked_Alt < Other_Tracked_Alt` → `>=` | ROR |
| Mutant18 | `Own_Above_Threat` line 16 | `Other_Tracked_Alt < Own_Tracked_Alt` → `>=` | ROR |
| Mutant19 | `Own_Below_Threat` line 13 | `Own_Tracked_Alt < Other_Tracked_Alt` → `<=` | ROR |
| Mutant20 | `Own_Above_Threat` line 16 | `Other_Tracked_Alt < Own_Tracked_Alt` → `<=` | ROR |

---

## PT (`code/PT/Mutants/printtokens_v*`)

3 mutants used in the final experiment. The `code/PT/Mutants/` directory contains 38
candidate versions (v1–v38 plus v0 baseline); most were excluded because they timed out,
had an unusable mutation rate, or produced no MR violations under the designed MRs. The
selection process is logged in `code/PT/Mutants/readme`.

The three retained versions are internally numbered **1, 2, 11** in the test harness (mapping
directly to the directory indices `printtokens_v1`, `printtokens_v2`, `printtokens_v11`). Each
directory contains a compiled `print_tokens` binary with a single fault in `print_tokens.c`.

| Version | Source file line | Change |
|---------|-----------------|--------|
| v1  | print_tokens.c:463 | `base[state]+ch >= 0` → `base[state]-ch >= 0` (AOR: `+` → `-`) |
| v2  | print_tokens.c:465 | `check[base[state]+ch] == state` → `check[base[state]-ch] == state` (AOR: `+` → `-`) |
| v11 | print_tokens.c:229 | `check_delimiter(ch)==TRUE` → `check_delimiter(ch)!=TRUE` (ROR: `==` → `!=`) |

---

## PT2 (`code/PT2/Mutants/printtokens2_v*`)

11 mutants used in the final experiment. The `code/PT2/Mutants/` directory contains 49
candidate versions (v1–v49 plus v0 baseline); most were excluded because they timed out,
had an unusable mutation rate, produced no MR violations, or all MGs were satisfied (even if
some were false-satisfied). The selection process is logged in `code/PT2/Mutants/readme`.

The eleven retained versions are internally numbered **4–14** in the test harness (mapping
to `printtokens2_v4` … `printtokens2_v14`). Each directory contains a compiled
`print_tokens2` binary with a single fault in `print_tokens2.c`.

| Version | Source file line | Change |
|---------|-----------------|--------|
| v4  | print_tokens2.c:162 | `is_eof_token(buffer)==TRUE` → `!=TRUE` (ROR) |
| v5  | print_tokens2.c:163 | `is_spec_symbol(buffer)==TRUE` → `!=TRUE` (ROR) |
| v6  | print_tokens2.c:164 | `ch=='"'` → `ch!='"'` (ROR) |
| v7  | print_tokens2.c:165 | `ch==59` → `ch!=59` (ROR) |
| v8  | print_tokens2.c:168 | `is_token_end(id,ch)==FALSE` → `!=FALSE` (ROR) |
| v9  | print_tokens2.c:175 | `is_eof_token(ch1)==TRUE` → `!=TRUE` (ROR) |
| v10 | print_tokens2.c:177 | `ch==EOF` → `ch!=EOF` (ROR) |
| v11 | print_tokens2.c:180 | `is_spec_symbol(ch1)==TRUE` → `!=TRUE` (ROR) |
| v12 | print_tokens2.c:182 | `ch==EOF` → `ch!=EOF` (ROR, second occurrence) |
| v13 | print_tokens2.c:185 | `id==1` → `id!=1` (ROR) |
| v14 | print_tokens2.c:190 | `id==0 && ch==59` → `id!=0 && ch==59` (ROR) |

---

## PrimeCount (`code/PrimeCount/Mutants/PrimeCount_v*`)

17 mutants (v1–v17; v0 is the fault-free baseline) collected from a prior PrimeCount
benchmark. All faults are single-line mutations in the C source (`primesieve` library).

| Mutant | File location (C source) | Change |
|--------|--------------------------|--------|
| v1  | line 615 | `g0 = g1` → `g0 -= g1` (AOR in integer square-root helper) |
| v2  | line 1277 | `bitarray[bits/CHAR_BIT]` → `bitarray[bits%CHAR_BIT]` (index `/` → `%`) |
| v3  | line 1281 | `maxp = isqrt(…)+1` → `maxp /= isqrt(…)+1` (AOR: `=` → `/=`) |
| v4  | line 1383 | `memset(…, ~0, …)` → `memset(…, ~-1, …)` (operand: `~0` → `~-1`) |
| v5  | line 1384 | `bytes += sizeof(uint64)-bytes%sizeof(uint64)` → `bytes = …` (AOR: `+=` → `=`) |
| v6  | line 1384 | `bytes += …` → `bytes -= …` (AOR: `+=` → `-=`) |
| v7  | line 1384 | `bytes += …` → `bytes *= …` (AOR: `+=` → `*=`) |
| v8  | line 1381 | `bytes += …` → `bytes /= …` (AOR: `+=` → `/=`) |
| v9  | line 1381 | `bytes += …` → `bytes %= …` (AOR: `+=` → `%=`) |
| v10 | line 1381 | `bytes%sizeof(uint64)` → `bytes+sizeof(uint64)` (AOR: `%` → `+` in RHS) |
| v11 | line 1381 | `bytes%sizeof(uint64)` → `bytes-sizeof(uint64)` (AOR: `%` → `-` in RHS) |
| v12 | line 1381 | `bytes%sizeof(uint64)` → `bytes/sizeof(uint64)` (AOR: `%` → `/` in RHS) |
| v13 | line 1451 | `(…WheelIndex)/8` → `(…WheelIndex)%8` (AOR: `/` → `%`) |
| v14 | line 456 | `sizeof(PreSieved)*WHEEL30` → `sizeof(PreSieved)/WHEEL30` (AOR: `*` → `/`) |
| v15 | line 591 | `x /= n` → `x *= n` (AOR: `/=` → `*=` in log computation) |
| v16 | line 1260 | `sieve_size%WHEEL30` → `sieve_size+WHEEL30` (AOR: `%` → `+` in index) |
| v17 | line 1451 | `(…WheelIndex)/8` → `(…WheelIndex)-8` (AOR: `/` → `-`) |

---

## SeqMap (`code/SeqMap/Mutants/seqmap_v*`)

5 mutants (v1–v5; v0 is the fault-free baseline) collected from a prior SeqMap benchmark.
v4 and v5 are source-identical (same fault, compiled separately); only one is counted in the
final experiment. All faults are single-line mutations in the C++ source (`seqmap` aligner).

| Mutant | File location (C++ source) | Change |
|--------|---------------------------|--------|
| v1 | line 572 | `for (j = 0; j < 4; j++)` → `j >= 4` (ROR: `<` → `>=`; loop never executes) |
| v2 | line 572 | `for (j = 0; j < 4; j++)` → `j == 4` (ROR: `<` → `==`; loop never executes) |
| v3 | line 577 | `count1(masks[0] & 65535)` → `count1(masks[1] & 65535)` (ORR: index 0 → 1) |
| v4 | line 574 | `mask0_table[i][j] = shift_key(i, submask)` → `&= shift_key(i, submask)` (AOR: `=` → `&=`) |
| v5 | line 574 | identical to v4 — duplicate entry in benchmark, not counted separately |

---

## grep (`code/grep/Mutants/grep_v*`)

10 mutants reused from prior MT studies on grep [39, 42]. The directory contains v0–v11;
v0 is the fault-free baseline and v3 is excluded (produced no usable MR violation signal).
All faults are single-line mutations in `grep-2.5.1a/src/dfa.c`.

| Mutant | dfa.c line | Change | Operator | Source |
|--------|------------|--------|----------|--------|
| v1  | 7156 | `(syntax_bits & RE_NO_BK_PARENS) == 0` → `!= 0` | ROR | Dai [39] |
| v2  | 8788 | `++j` → `--j` | AOR | Barus [42] |
| v4  | 1729 | `nfirstpos[-1]` → `nfirstpos[+1]` | AOR | Barus [42] |
| v5  | 7607 | `i < s->nelem` → `i >= s->nelem` | ROR | Barus [42] |
| v6  | 7163 | `(syntax_bits & RE_NO_BK_PARENS) == 0` → `!= 0` | ROR | Barus [42] |
| v7  | 8708 | `malloc(newsize + 1)` → `malloc(newsize - 1)` | AOR | Barus [42] |
| v8  | 8003 | `d->follows[i].nelem < merged.nelem` → `>` | ROR | Barus [42] |
| v9  | 7142 | `(syntax_bits & RE_NO_BK_VBAR) == 0` → `!= 0` | ROR | Barus [42] |
| v10 | 8162 | `k < CHARCLASS_INTS` → `k >= CHARCLASS_INTS` | ROR | Barus [42] |
| v11 | 7912 | `nlastpos[-2] += nlastpos[-1]` → `-=` | AOR | Barus [42] |

---

## Reproducing the mutant generation

For the small Python subjects (TSQ / DM / SMM / Tcas), the mutants are hand-edited copies of
the original program; no automated generation is required. The fault is marked in each file
with an inline comment of the form `# original_expr --> mutated_expr` adjacent to the
changed line.

For PrimeCount and SeqMap, the mutants are pre-compiled binaries distributed with the
benchmarks. Each version directory contains a `readme` with the unified diff of the fault.

For PT, PT2, and grep, the mutants are taken directly from the SIR repository and from prior
MT studies, respectively. The mutation operators applied (and the original mutator scripts
where available) are documented next to each program:

- `code/PT/mutator2.py`
- `code/PT2/mutator2.py`
- grep uses the SIR-release mutants distributed in `code/grep/Mutants/`
