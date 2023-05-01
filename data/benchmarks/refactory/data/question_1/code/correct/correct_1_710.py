def search(x, seq):
    pos = 0
    for ele in seq:
        if x <= ele:
            return pos
        else:
            pos += 1
    return pos
