def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    return
def search(x, seq):
    if list(seq) == []:
        return 0
    else:
        for element in seq:
            if x <= element:
                return list(seq).index(element)
            elif x > max(seq):
                return (list(seq).index(max(seq)))+1
