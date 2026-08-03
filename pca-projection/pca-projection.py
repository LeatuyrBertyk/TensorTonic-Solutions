import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """  
    X = np.array(X)
    (n, d) = X.shape

    # Step 1
    X = X - np.mean(X, axis = 0)

    # Step 2
    C = 1/(n-1) * X.T @ X

    # Step 3
    eigenvalues, eigenvectors = np.linalg.eigh(C)
    
    idx = np.argsort(eigenvalues)[::-1]
    idx = idx[:k]
    eigenvalues = eigenvalues[idx]
    W = eigenvectors[:, idx]

    # Step 4
    X_proj = X @ W

    return X_proj