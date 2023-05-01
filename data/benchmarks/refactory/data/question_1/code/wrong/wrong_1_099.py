def search(x, seq):
    for i in range (len(seq)):
        if x < seq[i]:
            return i
        elif x ==seq[i]:
            return i
        else:
            continue
    return i + 1
