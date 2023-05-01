def search(x, seq):
    i=0
    while i<len(seq):
        if x<=seq[i]:
            break
        i=i+1 
    return i
