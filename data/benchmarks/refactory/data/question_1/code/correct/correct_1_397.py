def search(x, seq):
    for i, ele in enumerate(seq):
        if ele >= x:
            return i
    return len(seq)
