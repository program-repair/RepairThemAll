def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == () or seq == [] or x <= seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i,j in enumerate(seq[:len(seq)-1]):
            if x > j and x <= seq[i+1]:
                return i+1
