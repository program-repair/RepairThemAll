def search(x, seq):     #seq is sorted
    pos = 0
    for i in range(len(seq)):
        elem = seq[i]
        if x <= elem:
            pos = i
            break
        else:
            pos += 1
    return pos
