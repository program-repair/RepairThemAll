def search(x, seq):
    for i, elem in enumerate(seq):
        if elem >= x: 
            return i #return the position of elem
    return len(seq) #if x > the largest value of seq, return the last position (len(seq))
    
