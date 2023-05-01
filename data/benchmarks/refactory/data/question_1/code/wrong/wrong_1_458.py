def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            continue
        return len(seq)
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
