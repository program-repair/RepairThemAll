def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x <= seq[-1]:
        for i in range(len(seq)):
            if seq[i] < x:
                continue
            else:
                return i
    else:
        return len(seq)
