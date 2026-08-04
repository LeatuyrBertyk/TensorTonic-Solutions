import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    x = np.array(x, dtype=float)

    elu_cal = np.where(x > 0, x, alpha*(np.exp(x)-1))
    
    return list(elu_cal)