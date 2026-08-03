import numpy as np
import math

def compute(x):
    if x == 0:
        return 0
    return x*math.log(x)/math.log(2)

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    n = len(y)
    cl, freq = np.unique(y, return_counts=True)

    prop = freq/n

    h = 0
    for i in range(len(cl)):
        h -= compute(prop[i])

    return float(h)