def search(x, seq):
    for i, ele in enumerate(seq, 0):
        if x > ele:
            i += 1
        else:
            break
    return i
