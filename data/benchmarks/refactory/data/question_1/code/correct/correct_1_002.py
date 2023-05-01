def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    output = 0
    while output < len(seq):
        if x > seq[output]:
            output += 1
        else:
            break
    return output
