def search(x, seq):
    if type(seq) == tuple:
        lst = list(seq)
    else:
        lst = seq

    counter = 0
    for i in lst:
        if x <= i:
            continue
        else:
            counter += 1
    return counter
