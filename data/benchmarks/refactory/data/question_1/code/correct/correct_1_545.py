def search(x, seq):
    n = len(seq)
    if n == 0:
        return 0
    else:
        for i in range(len(seq)):
            if x < seq[0]:
                return 0
            elif x <= seq[i] and x >= seq[i-1]:
                return i
            elif x > seq[n-1]:
                return n
                
