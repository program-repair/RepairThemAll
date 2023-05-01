def search(x, seq):
    for i in range(len(seq)):
        if x < seq[i]:
            return i
        elif seq[i] == seq[-1]:
            return i+1
        elif seq[i]<x<=seq[i+1]:
            return i
    return len(seq)+1     
        
