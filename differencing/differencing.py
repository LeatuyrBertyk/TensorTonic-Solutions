def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    for k in range(order):
        d = len(series)

        for i in range(d-1):
            series[i] = series[i + 1] - series[i]
        last = series.pop()

    return series