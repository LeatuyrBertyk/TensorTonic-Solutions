import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    e = np.abs(y_true - y_pred)
    quadratic = 0.5 * e** 2
    linear = delta * (e - 0.5 * delta)
    return np.where(e <= delta, quadratic, linear).mean()