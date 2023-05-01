def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i] and i == 0:
            return 0
        elif seq[i-1] < x <= seq[i]:
            return i
        elif x > seq[i] and i == len(seq)-1:
            return len(seq)
