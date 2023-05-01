def search(x, seq):
    for i in range(len(seq)-1):
        if seq[i] < x:
            return i
    return len(seq)
