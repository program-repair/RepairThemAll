def search(x, seq):
    counter=0
    for i in seq:
        if x>i:
            counter+=1
    return counter
