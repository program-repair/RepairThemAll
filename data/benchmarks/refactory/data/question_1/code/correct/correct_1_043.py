
def search(x, seq):
    n=len(seq)
    count=0
    for i in range(n):
        if seq[i]<x:
            count+=1
    return count
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
   
