def search(x, seq):
    new = list(enumerate(seq))
    for n in new:
        if x <= n[1]:
            return n[0]
    return len(seq)
