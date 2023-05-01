def search(x, seq):
    if len(seq) == 0:
        return 0
    else:
        for i,elem in enumerate(seq):
            if x > elem:
                continue
            return i
        return i+1
