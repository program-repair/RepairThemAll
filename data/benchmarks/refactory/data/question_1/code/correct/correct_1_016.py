def search(x, seq):
    if seq==() or seq==[]:
        return 0
    for a,b in enumerate(seq):
        if x<=b:
            return a
    for i in seq:
        if x>i:
            return a+1
