def search(x, seq):
    for i, y in enumerate(seq):
        if x <= y:
            return i
    if seq == [] or seq == (): 
        return 0
    else:
        return 1+i
