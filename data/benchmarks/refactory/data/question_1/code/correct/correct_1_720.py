def search(x, seq):
    seq = list(seq)
    index = 0
    for i in range (len(seq)):
        if x <= seq[i]:
            break
        elif x > seq[i]:
            index = i + 1
    return index
