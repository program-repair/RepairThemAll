def search(x, seq):
    pos=0
    for i in seq:
        if x<=i:
            pos=seq.index(i)
            return pos
    return len(seq)
