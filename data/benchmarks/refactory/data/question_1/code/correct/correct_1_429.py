def search(x, seq):
    position = 0
    for i in seq:
        if x <= i:
            break
        position = position + 1
    return position
