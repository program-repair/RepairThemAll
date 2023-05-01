def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if type(seq) == tuple:
        new_seq = list(seq)
        sort = []
        for i in range(len(new_seq)):
            if new_seq[i]<=x:
                sort.append(new_seq[i])
            else: 
                sort.append(x)
                sort.extend(new_seq[i:])
                break
        return sort
    else:
        sort = []
        for i in range(len(seq)):
            if seq[i]<=x:
                sort.append(seq[i])
            else: 
                sort.append(x)
                sort.extend(seq[i:])
                break
        return sort

