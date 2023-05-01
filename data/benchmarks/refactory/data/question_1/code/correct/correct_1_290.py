def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i, j in enumerate(seq):
        if x <= j:
            return i
    return len(seq)
