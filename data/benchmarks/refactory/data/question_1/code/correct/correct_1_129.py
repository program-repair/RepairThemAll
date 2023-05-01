def search(x, seq):
    if len(seq) == 0:
        return 0
    else:
        for i in seq:
            if x <= i:
                return seq.index(i)
            elif x > max(seq):
                return len(seq)
