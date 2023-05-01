def search(x, seq):
    lst = []
    for i, elem in enumerate(seq):
        lst.append((i, elem))
    for i in lst:
        if x <= i[1]:
            return i[0]
    return len(seq)
