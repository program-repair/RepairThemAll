def search(x, seq):
    if seq == ():
        return
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
            elif x >= max(seq):
                return len(seq) 
            else:
                continue 

