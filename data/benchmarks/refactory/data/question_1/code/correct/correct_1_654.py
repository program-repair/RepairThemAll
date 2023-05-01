def search(x, seq):
    counter = 0
    for elem in seq:
        if x > elem:
            counter += 1
        else:
            break
    return counter
