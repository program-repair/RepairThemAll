def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    lst = list(seq)
    lst.append(x)
    lst.sort()
    tup = tuple(enumerate(lst))
    for i in range(len(tup)):
        if tup[i][1]==x:
            return tup[i][0]
