def search(x, seq):
    if len(seq)==0:
        return 0
    a = list(enumerate(seq))
    for item in a:
        if x <= item[1]:
            return item[0]
    if x > seq[-1]:
        return len(seq)
