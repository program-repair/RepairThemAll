def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == []:
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
        if i == (len(seq)-1):
            return len(seq)
