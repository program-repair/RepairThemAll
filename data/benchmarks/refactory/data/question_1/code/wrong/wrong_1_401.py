def search(x, seq):
    for i, elem in enumerate(seq):
        if x > elem:
            continue
        else:
            return i
