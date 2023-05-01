def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    enumerated_list =()
    for i, elem in enumerate(seq):
        enumerated_list = enumerated_list + ((i,elem),)

    for number in enumerated_list:
        if x <= number[1]:
            res = number[0]
            break
        else:
            res = len(seq)
    return res
