def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    encoding = dict()
    for c in categories:
        if c not in encoding:
            count = 0
            sum_target = 0
            for i in range(len(categories)):
                cat = categories[i]
                if cat == c:
                    count += 1
                    sum_target += targets[i]
            encoding_c = sum_target / count
            encoding[c] = encoding_c
    for i in range(len(categories)):
        categories[i] = encoding[categories[i]]

    return categories
            