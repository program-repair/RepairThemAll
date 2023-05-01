def search(x, seq):
    for i, elem in enumerate(seq):
        if seq == ():
            return 0
        elif x == elem:
            return i
        elif x < elem:
            return i
        elif x > seq[-1]:
            return len(seq)
