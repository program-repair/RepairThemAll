def search(x, seq):
    for a, element in enumerate(seq):
        if x <= element:
            return a
    return len(seq)
