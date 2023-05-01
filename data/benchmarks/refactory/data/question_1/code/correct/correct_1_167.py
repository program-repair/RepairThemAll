def search(x, seq):
    pos = len(seq)
    for i, elem in enumerate(seq):
        if x <= elem:
            pos = i
            break
    return pos
