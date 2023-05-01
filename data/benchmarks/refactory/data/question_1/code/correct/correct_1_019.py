def search(x, seq):
    counter = 0
    while counter < len(seq):
        if x <= seq[counter]:
            return counter
        counter += 1
    return counter
