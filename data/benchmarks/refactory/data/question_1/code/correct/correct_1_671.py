def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if len(seq) == 0:
        return 0
    else:
        index = -1
        for i in seq:
            if x <= i:
                index += 1
                return index
            elif x > seq[-1]:
                return len(seq)
            else:
                index += 1


def search(x, seq):
    new=list(seq)
    new.append(x)
    new.sort()
    y=tuple(enumerate(new))
    for i in range(len(y)):
        if y[i][1]==x:
            return y[i][0]
