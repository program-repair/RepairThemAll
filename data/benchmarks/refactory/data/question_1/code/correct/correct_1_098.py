def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i,ele in enumerate(seq):
        if x<=ele:    #if x is less/equal to the specific element in the list
            return i   #return the index to be inserted in
    return len(seq)
