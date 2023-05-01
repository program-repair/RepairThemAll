def search(x, seq):
    y = len(seq)
    if y == 0:
        return 0
    if x < seq[0]:
        return 0
    else:
        for i in range(y-1):
            if x > seq[i] and x <= seq[i+1]:
                return i + 1
        return y
