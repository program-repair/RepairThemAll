def search(x, seq):
    i = 0
    while (i<len(seq) and x<seq[i]):
        i += 1
    i -= 1
    return i
