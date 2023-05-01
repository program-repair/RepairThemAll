def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
            else:
                continue
