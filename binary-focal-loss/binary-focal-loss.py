import numpy as np

def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    y = np.array(targets, dtype=float)
    p = np.array(predictions,dtype=float)

    pt = np.where(y == 1, p, 1-p)
    fl = -alpha * (1-pt)**gamma * np.log(pt)

    return fl.mean()
    