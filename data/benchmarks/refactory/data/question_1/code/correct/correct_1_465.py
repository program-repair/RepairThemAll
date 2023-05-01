def search(x, seq):
    if len(seq)==0:
        return 0
    elif x<seq[0]:
        return 0
    elif x>seq[-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x>seq[i] and x<seq[i+1]:
                return i+1
            elif x==seq[i]:
                return i
