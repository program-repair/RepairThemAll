def search(x, seq):
    if seq == ():
        return 0
    if seq == []:
        return 0
    for c,value in enumerate(seq):
        if value>=x:
            return(c)
    else:
        return(c+1)
        
