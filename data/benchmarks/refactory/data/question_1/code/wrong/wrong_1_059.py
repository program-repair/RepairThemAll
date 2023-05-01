def search(x, seq):
    for i in range(0, len(seq)):
        if seq[i] < x:
            continue
        elif seq[len(seq) - 1] < x:
            return len(seq)
        else:
            return i
