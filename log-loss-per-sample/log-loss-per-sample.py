import numpy as np

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    n = len(y_true)
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    y_pred = np.clip(y_pred, eps, 1 - eps)
    
    L = []
    
    for i in range(n):
        loss_i = -(y_true[i] * np.log(y_pred[i]) + 
                   (1 - y_true[i]) * np.log(1 - y_pred[i]))
        L.append(loss_i)
    
    return L