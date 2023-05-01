def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == [] or seq == ():
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        for i in range(len(seq)-1):
            if seq[i] == x:
                return i
            elif seq[i] < x and seq[i+1] > x:
                return i+1
