def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    output = []
    for value in values:
        output.append(ordering.index(value))

    return output