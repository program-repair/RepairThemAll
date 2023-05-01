def search(x, seq):
    total = seq
    counter = 0
    while counter != len(seq):
        if x <= total[counter]:
            break
        else:
            counter += 1
    return counter
