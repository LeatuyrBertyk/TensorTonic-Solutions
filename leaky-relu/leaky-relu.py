import numpy as np

def relu(x, alpha=0.01):
    if x >= 0:
        return x
    return alpha*x

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    
    return np.array([relu(num,alpha) for num in x])