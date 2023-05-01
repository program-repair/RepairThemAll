def search(x, seq):
    a = len(seq)
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return a
