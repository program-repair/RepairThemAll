def search(x, seq):
    if len(seq) == 0:
        indx = 0
    else:
        if x < seq[0]:
            indx = 0
        elif x > seq[-1]:
            indx = seq.index(seq[-1]) + 1
        else:
            for i in seq:
                if x <= i:
                    indx = (seq.index(i))
                    break                    
        return indx
