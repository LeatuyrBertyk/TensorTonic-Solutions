import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    n = y_true.shape[0]

    mse = np.sum((y_pred - y_true)**2)

    return mse/n