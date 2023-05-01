def search(x,seq):
    if type(seq) == tuple:
        tup = ()
        for i in seq:
            if i < x:
                tup = tup + (i,)
            else:
                tup = tup + (x,)
                break
        return len(tup) - 1
        
    elif type(seq) == list:
        counter = 0
        for i in seq:
            if i < x:
                counter = counter + 1
        return counter
        
