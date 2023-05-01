def search(x, seq):
    for i in seq:
        if x<i:
            return i
    return len(seq)
