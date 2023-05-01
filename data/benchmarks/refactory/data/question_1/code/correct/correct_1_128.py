def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    pos = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            pos = i
            return pos
    return len(seq)
