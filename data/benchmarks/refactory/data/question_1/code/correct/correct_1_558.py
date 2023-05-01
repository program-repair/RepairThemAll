def search(x, seq):
    pos = 0
    for i, element in enumerate(seq):
        if x <= element:
            pos = i
            return pos
        else:
            pos += 1
    return pos
