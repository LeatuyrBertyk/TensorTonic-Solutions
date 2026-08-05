def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    output = []

    for i in range(len(tokens)):
        if tokens[i] not in stopwords:
            output.append(tokens[i])
    return output