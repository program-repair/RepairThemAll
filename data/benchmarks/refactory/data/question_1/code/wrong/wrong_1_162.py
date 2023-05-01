def search(x, seq):
    for i in range(len(seq)-1):
        if x<=seq[0]:
            return 0
        if seq[i]<=x<=seq[i+1]:
            return i+1
        if x>=seq[-1]:
            return len(seq)
