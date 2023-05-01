def search(x, seq):
    r=0
    for i in seq:
        if x>i:
            r+=1
    return r
