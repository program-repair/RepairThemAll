def search(x, seq):
    for i, element in enumerate(seq):
        if x < element:
            return i
    return len(seq)
