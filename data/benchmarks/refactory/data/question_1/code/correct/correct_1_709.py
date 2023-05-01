def search(x, seq):
    if not seq:
        return 0
    elif x < seq[0]:
        return 0
    else:
        i = 0
        while i in range(len(seq)):
            if x <= seq[i]:
                return i
            elif x > seq[len(seq)-1]:
                return len(seq)
            else:
                i += 1
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    return
