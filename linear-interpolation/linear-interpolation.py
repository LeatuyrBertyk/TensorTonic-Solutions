def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    for j in range(len(values)):
        if values[j] is None:
            v_left = values[j]
            v_right = values[j]
            left = j
            right = j

            for i in range(j-1,-1,-1):
                if values[i] is not None:
                    v_left = values[i]
                    left = i
                    break

            for i in range(j+1,len(values),1):
                if values[i] is not None:
                    v_right = values[i]
                    right = i
                    break

            value_j = v_left + (j-left)/(right-left)*(v_right-v_left)
            values[j] = value_j
    return values