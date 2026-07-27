import numpy as np

def is_zeroes(a):
    for x in a:
        if x != 0:
            return False
    return True       

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.array(a)
    b = np.array(b)

    if is_zeroes(a) | is_zeroes(b):
        return 0
    
    return (a @ b)/(np.linalg.norm(a)*np.linalg.norm(b))