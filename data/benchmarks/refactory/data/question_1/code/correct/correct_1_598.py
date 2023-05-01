def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    position = 0
    for i in seq:
        if x > i:
            position += 1
        else:
            continue
    return position
