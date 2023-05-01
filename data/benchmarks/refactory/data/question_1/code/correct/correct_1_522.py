def search(x, seq):
    #Takes in a value x and a sorted sequence seq, and returns the
    #position that x should go to such that the sequence remains sorted 
    i =0       
    for p in seq:
        if x <= p:
            return i
        i += 1
    return len(seq)
    
