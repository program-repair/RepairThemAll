def search(x, seq):
    index = 0
    for i in seq:
        if x>i:
            index+=1
        else:
            return index
            
    return index
