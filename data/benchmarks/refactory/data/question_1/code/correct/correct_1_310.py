def search(x, seq):
    i = 0
    for element in seq:
        if x > element:
            i = i + 1
    return i
