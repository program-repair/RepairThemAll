def search(x, seq):
    for i in range (len(seq)):
        if seq == ():
            return 0
        if x <= seq[i]:
            return i
        elif x > seq[len(seq)-1]:
            return len(seq)
