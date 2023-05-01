def search(x, seq):
    #Takes in a value x and a sorted sequence seq, and returns the
    #position that x should go to such that the sequence remains sorted 
            
    for i, x in enumerate(seq):
        if x < seq[i]:
            return i
    return len(seq)
    
