def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if len(seq) == 0:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    counter = 0
    for i in seq:
        counter = counter + 1
        if x > seq[counter]:
            continue
        elif x <= seq[counter]:
            return counter

