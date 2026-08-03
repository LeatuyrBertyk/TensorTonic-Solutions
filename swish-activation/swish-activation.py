import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x, dtype=float)

    return x/(1+np.exp(-x))