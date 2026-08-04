import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """
    anchor = np.array(anchor, dtype=float)
    positive = np.array(positive, dtype=float)
    negative = np.array(negative, dtype=float)

    if anchor.ndim == 1:
        anchor = anchor.reshape(1, -1)
        positive = positive.reshape(1, -1)
        negative = negative.reshape(1, -1)
    
    l = np.maximum(0.0, np.linalg.norm(anchor - positive, axis=1)**2 - np.linalg.norm(anchor - negative,axis=1)**2 + margin)
    return l.mean()