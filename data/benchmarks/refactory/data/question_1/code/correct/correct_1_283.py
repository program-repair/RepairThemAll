def search(x, seq):
    counter=0
    while counter<len(seq):
        if seq[counter]>=x:
            return counter
        counter+=1
    return len(seq)
