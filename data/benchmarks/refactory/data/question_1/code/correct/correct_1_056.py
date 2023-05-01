def search(x, seq):
    if len(seq)==0:
        return 0
    for i in range(0,len(seq)):
        if x<seq[i]:
            return i
        elif x==seq[i]:
            return i
        elif x>seq[len(seq)-1]:
            return len(seq)
