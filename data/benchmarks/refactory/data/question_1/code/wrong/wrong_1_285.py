def search(x, seq):
    for i in range(0, len(seq) + 1):
        if len(seq) == 0:
            return None
        elif x < seq[0]:
            return 0
        elif seq[i] < x <= seq[i+1]:
            return i + 1
        elif seq[len(seq)-1] < x:
            return len(seq)
