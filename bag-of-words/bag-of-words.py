import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    n = len(vocab)
    output = np.zeros((n,), dtype=int)

    count = dict()
    for token in tokens:
        if token in vocab:
            if token not in count:
                count[token] = 0
            count[token] += 1
    for i in range(n):
        v = vocab[i]
        if v in count.keys():
            output[i] = count[v]
    return output