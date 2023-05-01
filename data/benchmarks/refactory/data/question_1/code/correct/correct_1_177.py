def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == [] or seq == ():
        return 0
    else:
        for a in range(1,len(seq)):
            if seq[a] == x:
                return a
            elif seq[a-1] < x < seq[a]:
                return a
        else:
            if x > seq[-1]:
                return len(seq)
            elif x < seq[0]:
                return 0
