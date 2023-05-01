def search(x,seq):
    for i in range(len(seq)):
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            break
        elif x > max(seq):
            return len(seq)
    return i
