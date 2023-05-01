def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if len(seq)< 1:
        return 0
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i 
            else:
                if x > seq[-1]:
                    return len(seq) 
                else:
                    continue
