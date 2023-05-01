def search(x, seq):
    for i in range(len(seq)-1):
        if x <= seq[i+1]:
            return i
    return len(seq)
