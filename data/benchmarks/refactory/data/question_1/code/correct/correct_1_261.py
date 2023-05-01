def search(x, seq):
    counter = 0
    for a in seq:
        if x > a:
            counter = counter + 1
    return counter
