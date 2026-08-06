def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    n = len(series)
    pct = []

    eps = 1e-12
    for i in range(1, n):
        try:
            pct_i = (series[i] - series[i-1])/series[i-1]
        except:
            pct_i = 0
        pct.append(pct_i)

    return pct