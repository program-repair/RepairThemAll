def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if x<=seq[0]:
        return 0
    if x>seq[-1]:
        return len(seq)
    else:
        for i,elem in enumerate(seq):
            if x>elem and x<=seq[i+1]:
                return i+1
