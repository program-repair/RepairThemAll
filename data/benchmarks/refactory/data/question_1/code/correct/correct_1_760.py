
def search(x, seq):
    if seq==(): 
        return 0
    elif seq==[]:
        return 0
    else:
        for i in range(len(seq)):
            if seq[i] >= x:
                return i
        return len(seq)
    return
