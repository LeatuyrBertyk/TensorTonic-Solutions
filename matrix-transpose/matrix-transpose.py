import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    m = A.shape[0]
    n = A.shape[1]
    trans = np.empty((n, m))

    for i in range(m):
        for j in range(n):
            trans[j][i] = A[i][j]

    return trans
