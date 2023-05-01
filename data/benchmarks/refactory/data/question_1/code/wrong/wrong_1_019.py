def search(x, seq):
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    elif seq == ():
        return 0
    for i, elem in enumerate(seq):
            if x <= elem:
                return i 
