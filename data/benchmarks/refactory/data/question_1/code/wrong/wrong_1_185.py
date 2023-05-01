def search(x, seq):
    for i in seq:
        if x>i:
            continue
    return seq.index(i)-1
            

