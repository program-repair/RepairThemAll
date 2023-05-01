def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i,ele in enumerate(seq):
        if x<=ele:
            return i
    return len(seq)
