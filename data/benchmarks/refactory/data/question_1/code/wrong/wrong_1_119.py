def search(x, seq):
    if seq == [] or ():
        return 0
    elif x >= seq[-1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if elem >= x:
                return i
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    return
