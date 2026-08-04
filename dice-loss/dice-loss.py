import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    p = np.array(p, dtype=float)
    y = np.array(y, dtype=float)

    dice = (2*np.sum(p * y) + eps)/(np.sum(p) + np.sum(y) + eps)
    return 1 - dice