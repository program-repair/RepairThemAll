def search(x, seq):
    result = 0
    counter = 0
    while counter < len(seq):
        temp = seq[counter]
        if x <= temp:
            return counter
        counter = counter + 1
    if counter == 0 and len(seq)!= 0:
        return len(seq)
    return counter
