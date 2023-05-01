def search(x, seq):
    if x > seq[-1]:
        return len(seq)
    else:
        for num in range(len(seq)):
            if x > seq[num]:
                continue
            elif x <= seq[num]:
                return num 
    return 0
