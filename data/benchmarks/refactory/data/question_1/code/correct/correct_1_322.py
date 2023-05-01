def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for position in range(len(seq)):
        if x < seq[position] or x == seq[position]:
            return position
    return len(seq)
