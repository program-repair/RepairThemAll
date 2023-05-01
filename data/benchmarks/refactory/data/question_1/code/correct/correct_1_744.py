def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    i = 0
    for ele in seq:
        if ele>=x:
            break
        i += 1    
    return i
