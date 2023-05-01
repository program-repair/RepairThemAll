def search(x, seq):
    def find_index(tup,elem):
        for i, j in enumerate(tup):
            if j==elem:
                return i
    if seq==[] or seq==():
        return 0
    elif x<=seq[len(seq)-1]:
        for i in seq:
            if x<=i:
                return find_index(seq,i)
    elif x>seq[len(seq)-1]:
        return len(seq)
    
