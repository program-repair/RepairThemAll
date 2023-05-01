def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if len(seq) ==1:
        if x < seq[0]:
            return 0
        else:
            return 1
    for i in range(len(seq)):
        if i == 0:
            if x < seq[0]:
                return 0
        if x == seq[i]:
            return i
        if seq[i-1] < x < seq[i]:
            return i
    return len(seq)
