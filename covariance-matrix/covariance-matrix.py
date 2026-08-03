import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.array(X)
    mu = X.mean(axis=0, keepdims=True)
    X_center = X - mu
    if X.ndim == 1:
        X = X.reshape(1, -1)

    n, d = X.shape

    if n == 1:
      return None
    
    cov = 1/(n-1) * X_center.T @ X_center
    return cov
    
    