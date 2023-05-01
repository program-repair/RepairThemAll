def search(x, seq):
    if len(seq)==0:
        return 0
    else:
        for i,elem in enumerate(seq):
            if elem>=x:
                return i
            elif i+1==len(seq):
                return len(seq)
            else:
                continue
