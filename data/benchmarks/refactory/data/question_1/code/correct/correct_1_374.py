def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    seq2 = list(enumerate(seq,0))
    value = 0
    for element in seq2:
        if x > element[1]:
            value = element[0]+1
    return value
