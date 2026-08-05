import numpy as np

def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    cos = np.dot(x1, x2) / (np.linalg.norm(x1) * np.linalg.norm(x2))

    if label == 1:
        return float(1 - cos)
    return float(max(0.0, cos - margin))