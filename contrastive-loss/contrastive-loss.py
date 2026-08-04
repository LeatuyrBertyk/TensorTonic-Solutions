import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    y = np.array(y, dtype=float)

    if a.ndim == 1:
        a = a.reshape(1, -1)
        b = b.reshape(1, -1)

    d = np.linalg.norm(a - b, axis=1)
    l = y*d**2 + (1.0-y)*np.where(margin >= d, margin-d, 0)**2

    if reduction == "sum":
        return np.sum(l)
    return l.mean()