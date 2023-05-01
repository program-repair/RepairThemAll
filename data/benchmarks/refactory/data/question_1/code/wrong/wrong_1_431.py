def search(x, seq):
    for i,elem in enumerate(seq):
        if len(seq)==0:
            return 0
        elif elem>=x:
            return i
        elif i+1==len(seq):
            return len(seq)
        else:
            continue
