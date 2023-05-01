def search(x, seq):
    i = 0
    for i, element in enumerate(seq):
        if x <= element:
            return i
    return len(seq)
