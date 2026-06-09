# SMM source test cases

100 source pairs of sparse matrices are generated at runtime by
`code/SMM/SMM_test.py` using `random.seed(1)`. The matrices are random sparse
matrices of compatible dimensions (m×k and k×n) with sparsity ≈ 0.7 and
integer entries from [-5, 5]. See the top of `code/SMM/SMM_test.py` for the
exact generator.
