def search(x, seq):
    counter = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            break
        else:
            counter += 1
    return counter
