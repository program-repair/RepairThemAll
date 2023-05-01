def search(x, seq):
    if seq == ():
            return 0
    for i in range(len(seq)):
        if x > seq[-1]:
            return len(seq)
        elif x == seq[i]:
            return i
        elif x < seq[i]:
            return i
