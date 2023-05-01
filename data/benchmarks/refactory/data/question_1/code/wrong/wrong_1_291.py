def search(x, seq):
    for i in range(len(seq)):
        if x < seq[i]:
            continue
            
        return i
