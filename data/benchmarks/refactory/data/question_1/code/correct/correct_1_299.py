def search(x, seq):
##    """ Takes in a value x and a sorted sequence seq, and returns the
##    position that x should go to such that the sequence remains sorted """
    n = 0
    for num in seq:
        if x>num:
            n +=1
        else:
            return n
    return n
