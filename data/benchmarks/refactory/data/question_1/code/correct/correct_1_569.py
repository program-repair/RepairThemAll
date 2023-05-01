def search(x, seq):
    if len(seq) == 0 or x <= seq[0]:
        return 0
    elif x > seq[len(seq) - 1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
