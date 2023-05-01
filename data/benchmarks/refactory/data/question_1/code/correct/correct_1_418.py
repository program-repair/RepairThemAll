def search(x, seq):
    position = 0
    for ele in seq:
        if x > ele:
            position = position + 1
    return position
