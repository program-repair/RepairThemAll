def search(x, seq):
    if len(seq) == 0:
        return 0
    else:
        for i, elem in enumerate(seq):
            if x > elem and i < (len(seq)-1):
                continue
            elif x <= elem:
                return i
            else:
                return len(seq)
