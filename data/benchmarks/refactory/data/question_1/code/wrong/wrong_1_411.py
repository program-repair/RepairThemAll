def search(x, seq):
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return i + 1
