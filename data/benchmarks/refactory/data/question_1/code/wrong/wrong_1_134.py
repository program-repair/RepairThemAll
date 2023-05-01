def search(x, seq):
    for i, elem in enumerate(seq):
        if i == 0 and x < elem:
            return 0
        elif x == elem:
            return i
        elif x < elem:
            return i
        elif x > seq[-1]:
            return len(seq)
