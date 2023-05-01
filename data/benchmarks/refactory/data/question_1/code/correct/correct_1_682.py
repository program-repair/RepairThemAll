def search(x, seq):
    if seq == [] or seq == ():
        return 0
    for elem in seq:
        if x < elem:
            return seq.index(elem)
        elif x == elem:
            return seq.index(elem)
    return len(seq)
