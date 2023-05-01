def search(x, seq):
    counter=0
    for i in seq:
        if x > i:
            counter+=1
        else:
            break
    return counter
