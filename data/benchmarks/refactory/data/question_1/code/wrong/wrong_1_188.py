def search(x, seq):
    if seq ==[]:
        return 0
    if x<0:
        return 0
    elif x<max(seq):
        for i in range(len(seq)):
            if (x>=seq[i]) and (x<=seq[i+1]):
                return i+1
    else:
        return len(seq)
