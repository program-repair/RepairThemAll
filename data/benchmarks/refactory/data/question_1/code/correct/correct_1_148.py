def search(x, seq):
    index = []
    for i, elem in enumerate(seq):
        index += [[i, elem],]
    for i in index:
        if x <= i[1]:
            return i[0]
    else: return len(seq)
