def search(x, seq):
    if x <= seq[0]:
        position = 0
    for i in range(len(seq)):
        if x <= seq[i] and x >= seq[i-1]:
            position = i
    return position

