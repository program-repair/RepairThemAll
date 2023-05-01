def search(x, seq):
    result=0
    for i in seq:
        if x>i:
            result+=1
        
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    return result
