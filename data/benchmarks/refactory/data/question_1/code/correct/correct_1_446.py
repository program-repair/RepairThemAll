def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
        else:
            continue
    return len(seq)
