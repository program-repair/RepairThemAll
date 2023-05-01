def search(x, seq):
    for i in range(len(seq)):
        if seq == [] or ():
            return 0
        elif x > seq[-1]:
            return len(seq)
        elif x == seq[i]:
            return i
        elif x < seq[i]:
            return i
