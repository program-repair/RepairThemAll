def search(x, seq):
    if seq == []:
        return 0
    else:
        for i, elem in enumerate(seq):
            if x < elem: 
                return i
            elif x == elem:
                return i
            elif i == len(seq)-1:
                return i+1
            
