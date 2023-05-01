def search(x, seq):
    for elem in seq:
        if x <= elem:
            break
        position += 1
    return position
