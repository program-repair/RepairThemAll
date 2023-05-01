def search(x, seq):
    if seq == () or seq == []:
        return 0
    else:
        count = 0
        for i in range (0, len(seq)):
            if seq[i] > x:
                return i
            elif seq[-1] < x:
                return len(seq)
