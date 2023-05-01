def search(x, seq):
    for i in range(len(seq)):
        if seq[i] > x:
            seq.insert(x, i)
    return seq
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    return
