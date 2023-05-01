def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    count = 0
    for i in seq:
        if x > i:
            count = count + 1
    return count
