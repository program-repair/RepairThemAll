def search(x, seq):
    for i in len(range(seq)):
        if x <= i:
            return i
    return len(seq)
