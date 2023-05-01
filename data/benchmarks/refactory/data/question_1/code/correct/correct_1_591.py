def search(x, seq):
    counter = 0
    for i in range(len(seq)):
        if x > seq[i]:
            counter += 1
        else:
            break
    return counter
