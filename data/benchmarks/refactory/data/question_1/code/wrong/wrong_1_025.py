def search(x, seq):
    a = len(seq)
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return a
    else:
        for i in range(a):
            if x == seq[i]:
                return i
            elif x < seq[i]:
                return i
