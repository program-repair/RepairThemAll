def search(x, seq):
    i=0
    while i<len(seq):
        if x<=seq[i]:
            return i
        else:
            i+=1
    return len(seq)
