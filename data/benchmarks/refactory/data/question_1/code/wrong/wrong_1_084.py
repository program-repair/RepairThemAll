def search(x, seq):
    if x <= seq[0]:
        return 0
    for i in range(len(seq)-1):
        if seq[i] <= x <= seq[i+1]:
            return i + 1
    return len(seq)
