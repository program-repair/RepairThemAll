def search(x, seq):
    if seq == () or []:
            return 0
    for i in range (len(seq)):
        if x <= seq[i]:
            return i
        elif x > seq[len(seq)-1]:
            return len(seq)
