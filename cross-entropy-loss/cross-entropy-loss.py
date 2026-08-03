import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    n = y_true.shape[0]

    entropy = 0
    for i in range(n):
        entropy -= np.log(y_pred[i, y_true[i]])

    return entropy/n