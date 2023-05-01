def search(x, seq):
    for i, val in enumerate(seq):
        if x <= val:
            return i
    return len(seq)
