def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    n = 0
    a = 0
    while n < len(seq):
        if seq[n] < x:
            n = n + 1
            a = n
        else:
            break
    return a
