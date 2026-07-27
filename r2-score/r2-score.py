import numpy as np

def match(x, y):
    for i in range(len(x)):
        if x[i] != y[i]:
            return False

    return True

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    if match(y_true, y_pred):
        return 1.0
    
    n = len(y_true)
    y_mean = sum(y_true)/n

    num = den = 0
    for i in range(n):
        num += (y_true[i] - y_pred[i])**2
        den += (y_true[i] - y_mean)**2

    if den == 0:
        return 0.0
        
    return 1 - num/den

    