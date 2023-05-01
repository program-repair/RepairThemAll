def search(x, seq):
    for k in range(len(seq)): 
        if x <= seq[k]:
            return k
        elif x > seq[k]:
            continue
    return len(seq)  # if bigger than the last element 
