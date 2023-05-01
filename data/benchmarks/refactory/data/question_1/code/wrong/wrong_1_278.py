def search(x, seq):
    if x > seq[-1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
            else:
                continue
