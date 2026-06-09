# grep source test cases

The full pool of **171,634** test cases reused from prior MT studies on grep
is shipped as `testpool.txt` (one test case per line; format
`-<flags> <pattern> <input-file>`).

We **randomly select 1,000** source test cases from this pool with
`random.seed(1)`, following the same selection strategy as the prior studies
([14], [39] in the paper). Different MRs in `code/grep/MRs/MR.py` impose
different constraints on the structure of valid input test cases (e.g.,
specific patterns, character classes, or file formats), so not all of the
1,000 source test cases are applicable to every MR. The number of applicable
test cases for each of the 12 MRs is documented in
[`docs/grep_test_cases.md`](../../docs/grep_test_cases.md).

To reproduce the per-MR applicability counts:

```bash
cd code/grep
python -c "
import random
with open('../../data/grep/testpool.txt') as f:
    pool = [line.strip() for line in f if line.strip()]
random.seed(1)
sampled = random.sample(pool, 1000)
print(f'sampled {len(sampled)} test cases')
"
```
