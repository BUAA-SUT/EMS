# TODO before pushing to GitHub

The repository is ready to upload, with one important caveat: a few documentation files
contain placeholder text ("???", "fill in", "see ...") that you need to fill in with
domain knowledge that I cannot derive automatically from the code/data alone.

Skim through these once, then delete this file before pushing.

---

## 1. `docs/MRs.md` — fill in the per-MR descriptions

I left a stub table for each program with the first 1-3 MRs filled in as a template, plus a
pointer to the actual MR implementation file. Please fill in the natural-language
description, source-test-case constraint, and output relation for the remaining MRs by
reading the corresponding code:

| Program | MR file (read this) |
|---------|---------------------|
| TSQ, DM, SMM, Tcas | `code/<program>/<program>_test.py` |
| PT, PT2 | `code/<program>/TestCase.py` |
| PrimeCount, SeqMap | `code/<program>/genMR.py` |
| grep | `code/grep/MRs/MR.py` |

Total MRs to document: 83 (55 reused + 28 new).

## 2. `docs/mutants.md` — per-mutant operator and faulty line

I listed every mutant directory/file and which program it belongs to, but the mutation
operator + faulty line columns are blank. Reading each mutant file (or diffing against
`Original.py` / the SIR baseline) will give you these. Total: 84 mutants.

## 3. `docs/grep_test_cases.md` — per-MR applicability counts

I shipped the full 171,634-test pool as `data/grep/testpool.txt` and described the sampling
recipe. The actual numeric counts (out of 1,000 sampled source test cases) for each of the
12 grep MRs are placeholder `???`. They can be regenerated locally with the snippet at the
bottom of `docs/grep_test_cases.md`. Replace the `???` cells with the real numbers.

## 4. (Optional) Additional source files I left out

To keep the repo upload-friendly, I excluded:

- `PT/info/`, `PT/inputs/`, `PT/source.alt/`, `PT/testplans.alt/`, `PT/universe/`
  (≈ 100 MB of auxiliary SIR distribution files) — these are not needed for the experiment
  scripts to run.
- `PT2/info/`, `PT2/Mutants.zip` (zip archive containing the same files as `Mutants/`).
- `SM/Mutants/allMutants/` (197 MB; only the 5 mutant variants `seqmap_v1` … `seqmap_v5`
  used in the paper are kept).
- `grep/files/` (54 MB of intermediate test-frame partition files); we kept the
  `TestPool_grep_no_repeat` test pool only, renamed to `data/grep/testpool.txt`.

If you want to include these, copy them back into the corresponding directories.

## 5. Replace the existing GitHub repo

The current public repo is <https://github.com/BUAA-SUT/EMS> and the paper references it
as `[41]`. To upload:

```bash
cd "<EMS-main-revised>"
git init
git add .
git commit -m "Revised artifact with detailed README, scripts, MR/mutants documentation"
git remote add origin git@github.com:BUAA-SUT/EMS.git
git push -u origin main --force   # if you want to overwrite the existing repo
```

Or, if you want to preserve history, push to a new branch first and merge via PR.

## 6. Sanity check before pushing

```bash
# verify no absolute paths remain
grep -rE "/Applications|/Users/rendaixu" code/ docs/ 2>/dev/null

# verify the repo size
du -sh .   # should be ~61 MB

# run a smoke test (fastest is TSQ)
cd code/TSQ && python TSQ_test.py
```
