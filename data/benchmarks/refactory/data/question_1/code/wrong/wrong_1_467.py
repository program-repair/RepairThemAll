def search(x, seq):
    if seq == [] or seq == (): 
        return 0
    elif len(seq) == 1:
        if seq[0] < x:
            return 0
        else: 
            return 1
    elif seq[-1] <= x:
        return len(seq)
    elif seq[0] >= x:
        return 0
    else:
        for i in range(len(seq)):
            if x >= seq[i] and x <= seq[i+1]:
                return i + 1
