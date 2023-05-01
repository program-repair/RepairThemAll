def search(x, seq):
    if len(seq)==0:
        return 0
    for i in range(len(seq)):
        if x<= seq[i]:
            a=i
            break
        elif x> seq[len(seq)-1]:
            a=len(seq)
    return a
        
