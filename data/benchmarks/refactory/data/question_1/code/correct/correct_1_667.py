def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    position = 0
    for i in range(len(seq)):
        if x > seq[i]:
            position = i + 1
        elif x == seq[i]:
            position = i
    return position
