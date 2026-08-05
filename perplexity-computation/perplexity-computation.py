def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    n = len(actual_tokens)

    prod = 1
    for i in range(n):
        prod *= prob_distributions[i][actual_tokens[i]]
    p = prod**(-1/n)
    return p