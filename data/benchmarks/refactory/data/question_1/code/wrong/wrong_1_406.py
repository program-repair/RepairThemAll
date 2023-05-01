def search(x, seq):
    for i in seq:
        if x <= i:
            return seq.index[i]
        else:
            return (seq.index[-1] + 1)
