def search(x, seq):
    for i in range(len(seq)-1):
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            return i
        else:
            return len(seq)
