def search(x, seq):
    if seq == () or seq == []:
        return 0
    else:
        for i in range(1,len(seq)):
            if x == seq[i]:
                return i
            elif seq[i-1] < x < seq[i]:
                return i
        else:
            if x > seq[(len(seq))-1]:
                       return len(seq)
            elif x < seq[0]:
                       return 0
