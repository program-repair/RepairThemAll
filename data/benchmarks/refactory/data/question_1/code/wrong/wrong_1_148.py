#def search(x, seq):
#    """ Takes in a value x and a sorted sequence seq, and returns the
#    position that x should go to such that the sequence remains sorted """
#    return



def search(val,seq):
    if val <= seq[0]:
        position = 0
    elif val >= seq[-1]:
        position = len(seq)
    else:
        for item in seq:
            if val <= item:
                position = seq.index(item)-1
    return position
