def search(x, seq):
    for i, elem in enumerate(seq):
        if seq == ():
            return 1
        if x <= elem:
            return i
        elif x > max(seq):
            return len(seq)
        
        
       
            
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """

