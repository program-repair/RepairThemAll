def search(x, seq):
    result = 0
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == () or seq == []:
        return result

    
    for i, elem in enumerate(seq):
        if x <= elem:
            result = i
            break
            
        else:
            result = len(seq)
    return result
        
