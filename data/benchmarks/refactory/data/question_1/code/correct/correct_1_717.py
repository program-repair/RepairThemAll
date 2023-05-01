def search(x, seq):
    a = 0
    for i in seq:
        if x <= seq[a]:
            return a
        else:
            a += 1
    return a
