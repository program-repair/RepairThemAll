def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    seq = tuple(seq)
    if x == () or x == []:
        return None
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        i = 0
        while i <= len(seq)-1:
            if x <= seq[i]:
                return i
            elif x > seq[i]:
                i += 1
