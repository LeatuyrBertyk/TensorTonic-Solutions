import numpy as np

def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    r = np.array(recommendations, dtype=int)
    count = np.array(item_counts, dtype=float)

    r_len = r.shape[0]
    sum_log_count = np.sum(np.log10([count[i] for i in r]))/np.log10(2)
    
    novelty = np.log10(n_users)/np.log10(2) - sum_log_count/r_len

    return novelty