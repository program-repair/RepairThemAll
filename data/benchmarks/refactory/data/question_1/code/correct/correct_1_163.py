def search(x,seq):  
    if not seq:
        return 0
    for i,elem in enumerate(seq):
        if elem>=x:
            return i
    return len(seq)
