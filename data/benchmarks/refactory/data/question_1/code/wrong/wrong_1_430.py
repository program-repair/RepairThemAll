def search(x, seq):
    for i,elem in enumerate(seq):
        if seq==() or []:
            return 0
        elif elem>=x:
            return i
        elif i+1==len(seq):
            return len(seq)
        else:
            continue
