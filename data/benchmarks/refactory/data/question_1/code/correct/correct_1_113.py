def search(x, seq):
    for pos,ele in enumerate(seq):
        if ele >= x:
            return pos
    return len(seq)
