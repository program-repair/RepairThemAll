def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            return i-1
        else:
            return len(seq)
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
