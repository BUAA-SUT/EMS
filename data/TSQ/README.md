# TSQ source test cases

The 100 source test cases used in the experiments are generated at runtime by
`code/TSQ/TSQ_test.py` using `random.seed(1)` (see the top of the file). For
each call, three side lengths a, b, c ∈ [1.0, 10.0] are drawn uniformly at
random; only valid triangles (a+b>c, b+c>a, c+a>b) are kept. The first 100
samples form the source test set.

To regenerate them deterministically:

```bash
cd code/TSQ
python -c "
import random; random.seed(1)
samples = []
while len(samples) < 100:
    a = round(random.uniform(1.0, 10.0), 2)
    b = round(random.uniform(1.0, 10.0), 2)
    c = round(random.uniform(1.0, 10.0), 2)
    if a + b > c and b + c > a and c + a > b:
        samples.append((a, b, c))
for t in samples: print(t)
"
```
