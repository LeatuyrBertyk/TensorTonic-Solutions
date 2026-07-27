import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    n = len(v)
    matrix = np.full((n, n), 0, dtype='f')

    for i in range(n):
        matrix[i, i] = v[i]

    return matrix
