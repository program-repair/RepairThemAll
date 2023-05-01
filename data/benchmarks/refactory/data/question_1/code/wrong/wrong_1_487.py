def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq==[]:
        return 0
    searchlist = list(enumerate(seq))
    for i in range(len(searchlist)):
        if x <= searchlist[i][1]:
            return searchlist[i][0]
    return i+ 1
