def search(x, seq):
    value = 0
    for i in range(0, len(seq)):
        if (x > seq[i]):
            value += 1
        elif (x <= seq[i]):
            break
    return value
