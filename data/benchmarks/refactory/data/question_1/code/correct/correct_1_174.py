def search(x, seq):
    k = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            break
        k = i + 1
    return k
