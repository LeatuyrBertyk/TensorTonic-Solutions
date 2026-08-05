import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if max_len is None:
        max_len = max(len(seq) for seq in seqs)

    N = len(seqs)
    L = max_len

    x = np.full((N, L), pad_value, dtype=int)

    if N == 1:
        try:
            x[0, :max_len] = seqs[:max_len]
        except:
            x[0, :max_len] = seqs[0][:max_len]
        return x
    
    for i in range(N):
        l = min(max_len, len(seqs[i]))
        x[i, :l] = seqs[i][:l]

    return x
