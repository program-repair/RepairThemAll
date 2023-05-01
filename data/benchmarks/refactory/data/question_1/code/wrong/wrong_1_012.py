def search(x, seq):
    for i, elem in enumerate(seq):
        if elem <= x <= elem + 1:
            return i - 1
