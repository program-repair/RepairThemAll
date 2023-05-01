def search(x, seq):
    position = 0
    for i in seq:
        if x > i:
            position +=1
        else:
            return position
    if position ==len(seq)-1:
        return position+1
    else: 
        return position
