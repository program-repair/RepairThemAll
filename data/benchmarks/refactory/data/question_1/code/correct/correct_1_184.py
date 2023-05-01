def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i in range(len(seq)):
	    if seq[i] < x <= seq[i + 1]:
                return i + 1
	    elif x > seq[-1]:
    		return len(seq)
    return 0
