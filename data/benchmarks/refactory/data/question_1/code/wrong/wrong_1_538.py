def search(x, seq):
    for i in range(len(seq)):
        if seq[i]>=x:
            break
    return i
