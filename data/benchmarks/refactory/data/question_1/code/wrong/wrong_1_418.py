def search(x, seq):
    for i in range(len(seq)-1):
        if x >= seq[i] and x <= seq[i+1]:
            break
    return i
