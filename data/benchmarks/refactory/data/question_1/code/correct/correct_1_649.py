def search(x, seq):
    position = 0
    for elem in seq:
        if x <= elem:
            break
        position += 1
    return position
