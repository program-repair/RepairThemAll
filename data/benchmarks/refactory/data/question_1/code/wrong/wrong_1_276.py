def search(x, seq):
    t = 0
    for i in seq:
        if x >= i:
            return t
        t += 1
    return len(seq)-1
    
    
