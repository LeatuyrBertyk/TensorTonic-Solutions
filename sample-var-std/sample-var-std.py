import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    x = np.array(x, dtype=float)
    n = x.shape[0]
    mu = x.mean()
    x = x - mu
    
    variance = np.sum(x**2) / (n - 1)
    std = np.sqrt(variance)

    return variance, std