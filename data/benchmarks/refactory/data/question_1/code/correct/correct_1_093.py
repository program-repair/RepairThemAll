
def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == () or seq == []:
        return 0
    else:
        for i in range(0,len(seq)):
            if i == 0 and x<seq[0]:
                return 0
            elif i==len(seq)-1 and x>seq[len(seq)-1]:
                return len(seq)
            elif seq[i] <= x and x<= seq[i+1]:
                return i+1
