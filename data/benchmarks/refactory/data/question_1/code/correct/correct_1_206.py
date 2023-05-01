def search(x, seq):
    for i, elem in enumerate(seq):
        if elem>=x:
            return i
        else:
            continue
    return len(seq)
