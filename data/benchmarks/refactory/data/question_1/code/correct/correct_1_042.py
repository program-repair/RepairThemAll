def search(x, seq):
    listseq=list(seq)
    n=len(seq)
        
    for i in listseq:
        if x<=i:
            return listseq.index(i)
    return n

    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
   

