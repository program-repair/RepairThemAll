def search(x, seq): 
    Index = 0
    for i in range(0,len(seq)+1): 
        Index = i
        if int(x) < seq[0]:
            return 0    
        elif int(x)> list1[len(seq)-1]:
            return len(seq)        
        elif int(x) > seq[i]:
            continue        
    return Index
