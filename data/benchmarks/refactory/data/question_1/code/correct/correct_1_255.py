def search(x, seq):
    if seq == ():
        return 0
    elif seq == []:
        return 0
    else:
        for i, elem in enumerate(seq):
            if x > seq[-1]:
                return len(seq)
            elif  x > elem:
                continue
            else:
                return i
