def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    index_for_x = 0
    for index, element in enumerate(seq) :
        if element < x:
            index_for_x+=1
        else:
            break
    return index_for_x
