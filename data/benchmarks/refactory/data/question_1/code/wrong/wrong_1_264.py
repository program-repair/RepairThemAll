def search(x, seq):
    if seq[len(seq)-1] < x:
        return len(seq)
    elif seq[0] >= x:
                return 0
    else:
        for i in range(len(seq)-1):
            if seq[i] < x and seq[i+1] >= x:
                return i+1
                break
