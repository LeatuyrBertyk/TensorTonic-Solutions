def user_based_cf_prediction(similarities, ratings):
    """
    Predict a rating using user-based collaborative filtering.
    """
    s = similarities
    r = ratings
    num = 0
    den = 0
    for u in range(len(s)):
        if s[u] > 0:
            num += s[u] * r[u]
            den += s[u]

    try:
        r_hat = num/den
    except:
        r_hat = 0.0
    return r_hat