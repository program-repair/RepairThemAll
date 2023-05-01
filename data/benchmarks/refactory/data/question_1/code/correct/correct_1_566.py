def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    position = 0
    if seq == ():
    #Terminates if there is no list of tuple at all 
        return position
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
            #Termniates once the sorted position is found 
                position = i
                break
            elif i == len(seq)-1:
            #Teminates when it finished sorting through and all are smaller 
                position = len(seq)
        return position 
