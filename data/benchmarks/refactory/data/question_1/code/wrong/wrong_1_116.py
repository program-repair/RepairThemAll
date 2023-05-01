def search(x, seq):
    n = len(seq)
    if seq ==():
        return 0
    for i in range(0,n):
        currentvalue = seq[i]
        position = i
        if position >= 0 and x>currentvalue:
            position = i+1
        elif position >= 0 and x<= currentvalue:
            return position
    return position
