def search(x, seq):
    #Takes in a value x and a sorted sequence seq, and returns the
    #position that x should go to such that the sequence remains sorted 
            
    for i, p in enumerate(seq):
        if x < p:
            return i
    return len(seq)
    
