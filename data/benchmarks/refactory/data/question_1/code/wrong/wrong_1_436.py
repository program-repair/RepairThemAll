def search(x,seq):
    tup = ()
    if type(seq) == tuple:
        for i in seq:
            if i < x:
                tup = tup + (i,)
            else:
                tup = tup + (x,)
                break
        return len(tup) - 1
        
