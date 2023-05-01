def search(x, seq):
    position = 0
    for i in seq:
        if x > i:
            position += 1
        else:
            return position
    return position
