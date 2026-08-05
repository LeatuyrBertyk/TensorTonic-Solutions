import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.array(x, dtype=float)

    if x.ndim == 1:
        _max = np.max(x)
        num = np.exp(x - _max)
        den = np.sum(np.exp(x - _max))
        x = num/den
    else:
        _max = np.max(x, axis=1, keepdims=True)
        num = np.exp(x - _max)
        den = np.sum(np.exp(x - _max), axis=1, keepdims=True)
        x = num/den
    return x