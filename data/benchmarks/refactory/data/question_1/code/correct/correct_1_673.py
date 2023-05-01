def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    lst = list(seq)
    lst.append(x)
    lst.sort()
    y = tuple(enumerate(lst))
    for i in range(len(y)):
        if y[i][1]==x:
            return y[i][0]
