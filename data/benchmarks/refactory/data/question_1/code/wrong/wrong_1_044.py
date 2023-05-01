def search(x, seq):
    for i in range(1, len(seq)+1):
        if x < seq[i-1]:
            return i-1
        elif seq[i-1]<x<=seq[i]:
            return i
    return len(seq)+1     
        
