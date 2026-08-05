def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    output = dict()
    
    for word in sentences:
        try:
            for w in word:
                if w not in output:
                    output[w] = 1
                else:
                    output[w] += 1
        except:
            if word not in output:
                output[word] = 1
            else:
                output[word] += 1
    return output