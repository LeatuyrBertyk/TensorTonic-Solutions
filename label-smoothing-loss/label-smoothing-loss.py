import numpy as np
import math

def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    K = len(predictions)
    predictions = np.array(predictions, dtype=float)

    q = np.array([epsilon/K]*K, dtype=float)
    q[target] = (1-epsilon) + epsilon/K

    L = 0
    for i in range(K):
        L -= q[i]*math.log(predictions[i])

    return L