def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if len(seq) == 0:
        return 0
    else:
        index = -1
        for i in seq:
            if x <= i:
                index += 1
                return index
            elif x > seq[-1]:
                return len(seq)
            else:
                index += 1
