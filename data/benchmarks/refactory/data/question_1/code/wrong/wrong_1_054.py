def search(x, seq):
    a = list(enumerate(seq))
    for item in a:
        if x <= item[1]:
            return item[0]
    if x > seq[-1]:
        return len(seq)
