def search(x, seq):
    position = 0
    for i in range(len(seq)):
        if x > seq[i]:
            position = i + 1
        elif x == seq[i]:
            position = i
    return position
