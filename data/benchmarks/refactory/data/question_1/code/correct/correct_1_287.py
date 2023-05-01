def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    enumerated_list=enumerate(seq)
    for i,elem in enumerated_list:
        if x<=elem:
            return i
    return len(seq)
