def search(x, seq):
    if len(seq) == 0:
        return False
    else:     
        for i in range(len(seq)):
            if x < seq[i]:
                return i
            elif seq[i]<x:
                return i+1
         
        
