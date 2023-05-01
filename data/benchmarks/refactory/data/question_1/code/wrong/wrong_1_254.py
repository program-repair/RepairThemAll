def search(x, seq):
    a = list(enumerate(seq))
    seq = list(seq)
    i = 0
    while i < len(seq):
        if x < seq[i] and i == 0:
            seq.insert(a[i][0], x)
            i = i + 2
        elif x < seq[i] and x > seq[i-1]:
            seq.insert(a[i][0],x)
            i = i + 2
        elif x > seq[len(seq)-1]:
            seq.append(x)
            i = i + 2
        else:
            i = i + 1
            
            
    return seq
