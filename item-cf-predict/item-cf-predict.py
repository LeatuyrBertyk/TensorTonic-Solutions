def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """
    t = target
    r = user_ratings
    s = item_similarities

    num = 0.0
    den = 0.0

    for i in range(len(s)):
        if s[i] > 0 and r[i] != 0 and i != t:
            num += s[i]*r[i]
            den += s[i]
    try:
        r_hat = num/den
    except:
        r_hat = 0.0
    return r_hat