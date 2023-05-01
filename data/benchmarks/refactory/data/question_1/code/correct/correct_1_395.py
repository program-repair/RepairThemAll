def search(x, seq):
    lenth=len(seq)
    for i in range(0,lenth):
        if x>seq[i]:
            continue
        else:
            return i
    return lenth

