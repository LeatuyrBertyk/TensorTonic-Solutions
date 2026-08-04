def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    r = set()
    for rec in recommendations:
        r.update(rec)
    
    if n_items == 0:
        return 0.0

    return len(r)/n_items