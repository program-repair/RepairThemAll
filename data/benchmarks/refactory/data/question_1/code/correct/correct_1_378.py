def search(x, seq):
    for i in enumerate(seq):
        if x <= i[1]:
            if i[0] == 0:
                return 0
            else:
                return i[0]
    return len(seq)
