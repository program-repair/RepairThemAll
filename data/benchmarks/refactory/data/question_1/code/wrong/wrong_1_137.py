def search(x, seq):
    for i, elem in enumerate(seq):
        if len(seq) == 0:
            return 0
        elif i == 0 and x < elem:
            return 0
        elif x <= elem:
            return i
        elif i == len(seq) - 1:
            return len(seq)
