def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    x = []
    for i in range(len(values)):
        current = []
        for j in range(degree + 1):
            current.append(values[i]**j)
        x.append(current)
    return x
    