# DM source test cases

100 source matrices are generated at runtime by `code/DM/DM_test.py` using
`random.seed(1)`. Each matrix is a square integer matrix of size n×n where
n ∈ [2, 5] is sampled uniformly and each entry is drawn uniformly from
[-10, 10]. See the top of `code/DM/DM_test.py` for the exact generator.
