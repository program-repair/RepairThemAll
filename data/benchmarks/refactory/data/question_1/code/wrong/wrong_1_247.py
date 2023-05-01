def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i] and x >= seq[i-1]:
            position = i
    return position

