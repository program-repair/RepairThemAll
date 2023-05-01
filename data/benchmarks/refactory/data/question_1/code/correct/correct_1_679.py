def search(x, seq):
    c = 0
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i in seq:
        if x > i:
            c += 1
        else:
            return c
    return c
