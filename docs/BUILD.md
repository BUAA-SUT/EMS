# Building C/C++ subjects

Three of the nine programs (`PT`, `PT2`, `grep`) are written in C and one (`SeqMap`) in C++.
The repository ships only their **source** for every mutant; the pre-built binaries have
been intentionally omitted so that users build them locally with their own toolchain.

## Compilation recipes

Run from the repository root:

### PT (Print_tokens)

```bash
cd code/PT/Mutants
for d in printtokens_v*; do
  (cd "$d" && gcc -std=gnu89 -fprofile-arcs -ftest-coverage -o print_tokens print_tokens.c)
done
```

### PT2 (Print_tokens2)

```bash
cd code/PT2/Mutants
for d in printtokens2_v*; do
  (cd "$d" && gcc -std=gnu89 -fprofile-arcs -ftest-coverage -o print_tokens2 print_tokens2.c)
done
```

### grep

```bash
cd code/grep/Mutants
for d in grep_v*; do
  (cd "$d" && ./configure --disable-shared && make CFLAGS="-O0 -fprofile-arcs -ftest-coverage")
done
```

(grep distributes its own `configure`/`Makefile`; the `-fprofile-arcs -ftest-coverage`
flags enable `gcov` collection used by `code/grep/statement_cov_grep.py`.)

### SeqMap

```bash
cd code/SeqMap/Mutants
for d in seqmap_v*; do
  (cd "$d" && g++ -O0 -fprofile-arcs -ftest-coverage -o seqmap seqmap.cpp)
done
```

## Why we ship only sources

1. Pre-built binaries are not portable across macOS / Linux / Windows.
2. Binaries can leak local file-system paths via debug-info, which is undesirable for a
   public artifact.
3. Coverage tracing requires the binary to be built with the user's local `gcov`
   toolchain anyway.

After building, the corresponding `*_test.py` driver (e.g., `code/PT/PT_test.py`) can locate
the binary inside each `Mutants/<version>/` directory automatically.
