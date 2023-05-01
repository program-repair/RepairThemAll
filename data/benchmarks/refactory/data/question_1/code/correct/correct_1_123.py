def search(x, seq):
    ns = tuple(enumerate(seq))
    for y in ns:
        if x <= y[1]:
            return y[0]
    return len(seq)
