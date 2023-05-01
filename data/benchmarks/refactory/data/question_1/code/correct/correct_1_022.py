def search(x, seq):
    position = 0
    for i, elem in enumerate(seq):
        if x <= elem:
            position = i
            return position
        else:
            position = i + 1
    return position
