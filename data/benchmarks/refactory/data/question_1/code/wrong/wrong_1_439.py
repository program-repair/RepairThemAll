def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    a = 0
    for i in seq:
        if i>x:
            a = a+1
    return a
