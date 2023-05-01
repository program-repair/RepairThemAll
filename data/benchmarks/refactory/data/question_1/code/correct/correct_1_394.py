def search(x, seq):
    a = list(enumerate(seq))
    if seq == () or seq == []:
        return 0
    seq = list(seq)
    i = 0
    while i < len(seq):
        if x < seq[i] and i == 0:
            return 0
        elif x <= a[i][1] and x >= a[i-1][1]:
            return a[i][0]
        elif x > a[len(seq)-1][1]:
            return len(seq)
        else:
            i = i + 1
            
            
    return seq
    
