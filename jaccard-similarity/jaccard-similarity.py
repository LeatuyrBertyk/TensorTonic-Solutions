def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    set_a = set(set_a)
    set_b = set(set_b)

    intersection = set_a & set_b
    union = set_a | set_b
    
    try:
        return len(intersection) / len(union)
    except:
        return len(intersection) * 1e-12