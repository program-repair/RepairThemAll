def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == () or seq == []:
        return 0
    elif x < seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    for i in range(len(seq)):
        if x == seq[i]:
            return i
        elif x > seq[i-1] and x < seq[i]:
            return i
