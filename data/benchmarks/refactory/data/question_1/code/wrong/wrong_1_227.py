def search(x, seq):
    result = None
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i, elem in enumerate(seq):
        if x <= elem:
            result = i
            break
            
        else:
            result = len(seq)
    return result
        
