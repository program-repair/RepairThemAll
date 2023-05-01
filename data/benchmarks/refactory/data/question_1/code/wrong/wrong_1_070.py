def search(x, seq):
    for i in range(0,len(seq)):
        if len(seq)==0:
            return False
        elif x<seq[i]:
            return i
        elif x==seq[i]:
            return i
        elif x>seq[len(seq)-1]:
            return len(seq)
