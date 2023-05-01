def search(x, seq):
    for i, elem in enumerate(seq):
        if len(seq) == 0:
            return 0
        elif x > seq[-1]:
            return len(seq)
        elif  x > elem:
            continue
        else:
            return i
