def search(x, seq):
    a = len(seq)
    if a == 0:
        return 0
    if a !=0 and x < seq[0]:
        return 0
    elif a!= 0 and x > seq[-1]:
        return a
    else:
        for i in range(a):
            if x == seq[i]:
                return i
            elif x < seq[i]:
                return i
