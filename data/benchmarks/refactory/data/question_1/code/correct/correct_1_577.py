def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    position = 0
    for num in enumerate(seq):
        if x <= num[1]:
            position = position
        elif x > num[1]:
            position += 1
            
    return position

