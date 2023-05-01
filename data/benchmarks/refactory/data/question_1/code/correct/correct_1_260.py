def search(x,seq):
    if len(seq) == 0:
        return 0
    else:
        for i in range(len(seq)):
            if x > max(seq):
                return len(seq)
            elif x > seq[i]:
                continue
            elif x <= seq[i]:
                break
        return i
