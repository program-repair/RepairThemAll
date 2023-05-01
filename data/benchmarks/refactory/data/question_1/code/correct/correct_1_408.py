
def search(x, seq):
    if seq==(): 
        return 0
    elif seq==[]:
        return 0
    else:
        pos=0
        for i, elem in enumerate(seq):
            if elem >= x:
                return i
        return i+1
