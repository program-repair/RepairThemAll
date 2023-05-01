def search(x, seq):
    a = 0
    for i,j in enumerate(seq):
        if x > j and i < len(seq)-1:
            continue
        elif x <= j:
            a = i
            break
        else:
            a = len(seq)
    return a
