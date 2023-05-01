def search(x, seq):
    for i,elem in enumerate(seq):
        if elem>=x:
            return i
        elif i+1==len(seq):
            return len(seq)
        else:
            continue
