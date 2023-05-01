def search(x, seq):
    counter = 0
    for i in range(1, len(seq)+1):
        if x < seq[i-1]:
            counter = i-1
        elif seq[i-1]<x<seq[i]:
            counter = i
        counter = i
    return counter    
        
