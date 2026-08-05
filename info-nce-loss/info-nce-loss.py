import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    Z1 = np.array(Z1, dtype=float)
    Z2 = np.array(Z2, dtype=float)

    S = Z1 @ Z2.T / temperature
    S = S - np.max(S)

    T = np.exp(S)
    n = S.shape[0]

    T_diag = np.diag(T)
    T_prod_diag = np.prod(T_diag)

    T_sum_row = T @ np.ones((n,1))
    T_prod_sum_row = np.prod(T_sum_row)

    l = T_prod_diag / T_prod_sum_row
    L = -np.log(l)/n

    return L