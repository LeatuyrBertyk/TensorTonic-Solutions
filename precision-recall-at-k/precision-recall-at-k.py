def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    top_k = set(recommended[i] for i in range(k))
    relevant = set(relevant)

    precision = len(top_k & relevant)/k
    recall = len(top_k & relevant)/len(relevant)

    return [precision, recall]