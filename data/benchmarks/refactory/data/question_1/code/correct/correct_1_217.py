def search(x, seq):
    position = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            position = i
            break
        else:
            position = len(seq)
    return position
