def search(x, seq):
    for i in range(len(seq)):
        if seq[0]>0 and x<0:
            return 0
        elif x==seq[i] or x<seq[i]:
            return i
    else:
        return len(seq)
