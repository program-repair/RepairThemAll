
def search(x, seq):
    new_seq=list(seq)
    new_seq.append(x)
    sort=[]
    while new_seq:
        smallest=new_seq[0]
        for element in new_seq:
            if element<smallest:
                smallest=element
        new_seq.remove(smallest)
        sort.append(smallest)
    for i,elem in enumerate(sort):
        if elem==x:
            return i
