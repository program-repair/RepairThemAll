def search(x, seq):
    if x <= seq[-1]:
        for i in range(len(seq)):
            if seq[i] < x:
                continue
            else:
                return i
    else:
        return len(seq)
