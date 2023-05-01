def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i in enumerate(seq):
        if x <= i[1]:
            return i[0]
    return len(seq)
