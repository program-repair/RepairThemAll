def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    length = len(seq)
    for i, elem in enumerate(seq):
        if x < elem:
            return i
        else:
            if x == elem:
                return i
            if (i == length-1):
                return i+1
