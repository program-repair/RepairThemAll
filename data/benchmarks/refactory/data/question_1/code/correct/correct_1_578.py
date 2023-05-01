def search(x, seq):
    counter = 0
    for i in seq:
        if x>i:
            counter +=1 #all the element that is the smaller than x
    return counter
    
