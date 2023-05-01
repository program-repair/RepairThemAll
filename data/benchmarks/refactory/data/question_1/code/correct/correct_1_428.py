def search(x, seq):
    if len(seq) == 0:
        return 0
    else:
        for i in range(len(seq)):
            if x < seq[0]:
                pos = 0
                break
            elif x <= seq[i]:
                pos = i
                break
            elif x > seq[len(seq) - 1]:
                pos = len(seq)
                break
        return pos
