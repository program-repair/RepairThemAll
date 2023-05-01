def search(x, seq):
    if seq == ():
        return 0
    for i, elem in enumerate(seq):
        if x == elem:
            return i
        elif x < elem:
            return i
        elif x > seq[-1]:
            return len(seq)
