def search(x, seq):
    seq = list(seq)
    for i in range(len(seq)):
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            return i
    return len(seq)
