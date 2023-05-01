def search(x, seq):
    for i in range(len(seq)):
        if len(seq)==0:
            return 0
        elif x<=seq[i]:
            return i
    return i+1
