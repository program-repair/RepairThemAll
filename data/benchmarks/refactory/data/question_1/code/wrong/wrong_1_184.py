def search(x, seq):
    for i in seq:
        if x>i:
            continue
        else:
            return ((seq).index(i))-1
            

