import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x = np.array(x, dtype=float)
    n = x.shape[0]

    mu = x.mean()
    var = np.sum((x - mu)**2) / (n - 1)
    std = np.sqrt(var)
    
    t = (mu - mu0) / (std / np.sqrt(n))
    return t