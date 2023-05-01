def search(x, seq):
    if seq == () or []:
        return 0
    for c,value in enumerate(seq):
        if value>=x:
            return(c)
    else:
        return(c+1)
