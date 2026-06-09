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
| SMM         | 6        | `code/SMM/Mutant1.py … Mutant7.py`               |
| Tcas        | 20       | `code/Tcas/Mutant1.py … Mutant20.py`             |
| PT          | 3        | `code/PT/Mutants/printtokens_v*/`                |
| PT2         | 11       | `code/PT2/Mutants/printtokens2_v*/`              |
| PrimeCount  | 17       | `code/PrimeCount/Mutants/`                       |
| SeqMap      | 4        | `code/SeqMap/Mutants/seqmap_v*/`                 |
| grep        | 10       | `code/grep/Mutants/grep_v*/`                     |
| **Total**   | **84**   |                                                  |

> Note: Mutant numbering may include a `_v0` (or equivalent) **non-faulty baseline** in
> some programs (e.g. `grep_v0`, `seqmap_v0`, `printtokens_v0`). These baselines are kept
> for sanity checking and are *not* counted as faulty mutants.

---

## Per-mutant details

The following tables summarise, for each mutant, the mutation operator applied and the
faulty line / region. Author-filled details should match the contents of the actual mutant
files.

### TSQ (`code/TSQ/Mutant*.py`)

| Mutant | Operator | Faulty line(s) | Description |
|--------|----------|----------------|-------------|
| Mutant1 | … | … | *(fill in: e.g., relational-operator-replacement at line 22 changing `>` to `>=`)* |
| Mutant2 | … | … |  |
| Mutant3 | … | … |  |
| Mutant4 | … | … |  |
| Mutant5 | … | … |  |
| Mutant6 | … | … |  |

### DM (`code/DM/Mutant*.py`)

| Mutant | Operator | Faulty line(s) | Description |
|--------|----------|----------------|-------------|
| Mutant1 – Mutant7 | … | … | *(fill in)* |

### SMM (`code/SMM/Mutant*.py`)

| Mutant | Operator | Faulty line(s) | Description |
|--------|----------|----------------|-------------|
| Mutant1 – Mutant7 | … | … | *(fill in)* |

### Tcas (`code/Tcas/Mutant*.py`)

The 20 Tcas mutants are a mix of SIR-released versions and author-generated mutants. Mutation
operators are mostly arithmetic-operator-replacement (`+ → -`), relational-operator-replacement
(`< → ≤`), and boundary perturbations.

| Mutant | Source | Operator | Faulty line(s) | Description |
|--------|--------|----------|----------------|-------------|
| Mutant1 – Mutant20 | SIR / author | … | … | *(fill in)* |

### PT (`code/PT/Mutants/printtokens_v*`)

3 SIR-released mutants. Each mutant directory contains the mutated `print_tokens.c`. The
faulty lines are listed in `code/PT/info/fault-matrix` and `code/PT/info/hardmu`.

| Mutant directory | Operator | Faulty line(s) |
|------------------|----------|----------------|
| `printtokens_v1` | … | … |
| `printtokens_v…` | … | … |

### PT2 (`code/PT2/Mutants/printtokens2_v*`)

11 SIR-released mutants. Faulty lines are listed in `code/PT2/info/`.

| Mutant directory | Operator | Faulty line(s) |
|------------------|----------|----------------|
| *(fill in)* | … | … |

### PrimeCount (`code/PrimeCount/Mutants`)

17 mutants reused from a prior PrimeCount benchmark.

### SeqMap (`code/SeqMap/Mutants/seqmap_v*`)

4 mutants reused from prior MT studies on SeqMap.

### grep (`code/grep/Mutants/grep_v*`)

10 mutants reused from prior MT studies on grep [39].

---

## Reproducing the mutant generation

For the small Python subjects (TSQ / DM / SMM / Tcas / PrimeCount / SeqMap), the mutants are
hand-edited copies of the original program; no automated generation is required.

For PT, PT2, and grep, the mutants are taken directly from the SIR repository and from prior
MT studies, respectively. The mutation operators applied (and the original mutator scripts
where available) are documented next to each program:

- `code/PT/mutator2.py`
- `code/PT2/mutator2.py`
- (grep uses the SIR-release mutants distributed in `code/grep/Mutants/`)
