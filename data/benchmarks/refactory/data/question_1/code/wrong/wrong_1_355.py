def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    position = 0
    found = False
    
    while position < len(seq) and not found:
        if x < seq[position]:
            found = True
        else:
            position += position
    
    return position
