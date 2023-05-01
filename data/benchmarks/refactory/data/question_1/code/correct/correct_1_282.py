def search(x, seq):
    for a, i in enumerate(seq):
        if x <= i:
            return a
    return len(seq)

