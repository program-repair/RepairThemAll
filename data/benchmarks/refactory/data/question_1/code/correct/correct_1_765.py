def search(x, seq):
    n = 0 

    for i in seq:
        if x <= i:
            return n
        else:
            n += 1
            
    return n 
