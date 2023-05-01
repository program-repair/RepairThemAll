def search(x, seq): 
    if int(x) < seq[0]:
        return 0    
    elif int(x)> seq[len(seq)-1]:
        return len(seq)  
    Index = 0
    for i in range(0,len(seq)): 
        if int(x)>seq[i]:
            continue
        Index = i
        return Index
