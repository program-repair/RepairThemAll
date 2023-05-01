def search(x, seq):
    for i, ele in enumerate(seq):
        if x <= ele:
            return i
    return len(seq)
