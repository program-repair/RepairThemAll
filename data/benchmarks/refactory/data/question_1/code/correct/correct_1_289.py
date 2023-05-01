def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return seq.index(seq[i])
        elif seq[-1] <  x:
            return seq.index(seq[-1])+1
    return 0

