def search(x, seq):
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    elif seq == () or seq ==[]:
        return None
    for i, elem in enumerate(seq):
            if x <= elem:
                return i 
