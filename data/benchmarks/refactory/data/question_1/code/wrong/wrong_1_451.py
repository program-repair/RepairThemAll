def search(x, seq):
    for i in range(len(seq)):
        if seq[i] < x:
            continue
        elif x <= seq[i]:
            return i
        else:
            return len(seq)+1
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
