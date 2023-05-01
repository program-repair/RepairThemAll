def search(x,seq):
    for index in range(len(seq)):
        if x <= seq[index]:
            return index
    return len(seq)
        
