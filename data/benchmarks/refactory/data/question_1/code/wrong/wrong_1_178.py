def search(x, seq):
    for i, elem in enumerate(seq):
        if x > seq[-1]:
            return len(seq)
        elif  x > elem:
            continue
        else:
            return i
