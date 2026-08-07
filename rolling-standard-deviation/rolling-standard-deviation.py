import math 

def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    n = len(values)
    k = window_size

    output = []
    for i in range(n-k+1):
        mu = 0
        for j in range(k):
            mu += values[i+j]
        mu = mu/k

        sigma = 0
        for j in range(k):
            sigma += (values[i+j] - mu)**2
        sigma = math.sqrt(sigma/k)

        output.append(sigma)
    return output