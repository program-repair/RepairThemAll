def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x > seq[-1]:
        return len(seq)
    elif x < seq[0]:
        return 0
    else:
        for i in seq:
            if x > i:
                continue
            else:
                return seq.index(i) 
