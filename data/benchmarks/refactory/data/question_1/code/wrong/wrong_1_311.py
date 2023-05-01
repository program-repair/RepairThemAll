def search(x, seq):
    for i in range(len(seq)):
        if x<=seq[i]:
            break
    return i
