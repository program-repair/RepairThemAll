def search(x, seq):
    for i in range(len(seq)):
        pos = len(seq)
        if x <= seq[i]:
            pos = i
            break
    return pos

