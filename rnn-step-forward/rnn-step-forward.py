import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    x_t = np.array(x_t, dtype=float)
    h_prev = np.array(h_prev, dtype=float)
    Wx = np.array(Wx, dtype=float)
    Wh = np.array(Wh, dtype=float)

    h_t = np.tanh(x_t @ Wx + h_prev @ Wh + b)
    
    return h_t
