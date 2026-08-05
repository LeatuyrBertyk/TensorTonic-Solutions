import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x, dtype=float)
    n = x.shape
    
    mean = x.mean()
    median = np.median(x)

    count = Counter(x)
    mode = count.most_common(1)[0][0]

    return float(mean), float(median), float(mode)