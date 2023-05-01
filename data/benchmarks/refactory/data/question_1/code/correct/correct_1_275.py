def search(x, seq):
    counter = 0
    for value in seq:
        if x > value:
            counter = counter + 1
        else:
            break
    return counter
