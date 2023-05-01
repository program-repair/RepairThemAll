def search(x, seq):
    a = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            a = i
            break
        else:
            a = len(seq)
    return a
            
