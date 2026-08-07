def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    for k in range(len(X)):
        current = X[k]
        d = len(current)

        for i in range(d-1):
            for j in range(i+1,d):
                current.append(current[i] * current[j])

    return X