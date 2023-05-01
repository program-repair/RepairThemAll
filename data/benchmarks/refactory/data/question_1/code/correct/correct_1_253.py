def search(x, seq):
    for j, elem in enumerate(seq):
        if x<= elem:
            return j
    return len(seq)
