import numpy as np
import math 

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    if len(x) != len(y):
        raise ValueError
    
    dis = 0
    for i in range(len(x)):
        dis += (x[i] - y[i])**2

    return math.sqrt(dis)