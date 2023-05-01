def search(x, seq):
    for i, elem in enumerate(seq):
        if elem == x:
            return i
        elif x > elem:
            continue
        elif x < elem:
            return i
    return len(seq)
