def search(x, seq):
    if seq==[] or seq== ():
        return 0
    else:
        for i, elem in enumerate(seq):
            if elem>=x:
                return i
        else:
            return (i+1)
