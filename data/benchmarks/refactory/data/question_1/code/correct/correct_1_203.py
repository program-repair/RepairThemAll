def search(x, seq):
    if seq == () or seq == []:
        return 0
    else:
        for i in range (len(seq)):
            if x < seq[i]:
                return i
            elif x ==seq[i]:
                return i
            else:
                continue
    return i + 1
