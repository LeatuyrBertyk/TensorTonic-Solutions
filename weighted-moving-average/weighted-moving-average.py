def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    n = len(values)
    k = len(weights)
    
    sum_weights = 0
    for i in range(k):
        sum_weights += weights[i]
        
    wma = []
    
    for i in range(n-k+1):
        sum_x = 0
        for j in range(k):
            sum_x += weights[j] * values[i+j]
        wma.append(sum_x / sum_weights)

    return wma