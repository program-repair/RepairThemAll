def search(x, seq):
    for i, elem in enumerate(seq):
        if x == elem:
            return i
        elif x < seq[0]:
            return 0
        elif x < elem and x > seq[i-1]:
            return i

    return len(seq)

    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
