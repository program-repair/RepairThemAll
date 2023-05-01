def search(x, seq):
    if seq[0] >= x or seq == () or seq == []:
                return 0
    elif seq[len(seq)-1] < x:
        return len(seq)
    else:
        for i in range(len(seq)-1):
            if seq[i] < x and seq[i+1] >= x:
                return i+1
                break
