def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    counter = 0
    result = 0
    while counter < len(seq):
        if x < min(seq):
            result = 0
            break
        elif x > max(seq):
            result = len(seq)
            break
        elif x <= seq[counter]:
            result = counter
            break
        counter += 1
    return result
