def search(x, seq):
    for i in seq:
        if x <= i:
            return seq.index(i)
        elif x > max(seq):
            return len(seq)
