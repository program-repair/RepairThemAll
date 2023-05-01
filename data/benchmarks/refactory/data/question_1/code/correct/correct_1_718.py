def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    counter = 0
    if len(seq) == 0:
        return 0

    for i in seq:
        if x <= i:
            return counter
        else:
            counter += 1

    return counter
