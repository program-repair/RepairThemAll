def search(x, seq):
    if not seq:
        return 0
    elif x < seq[0]:
        return 0
    for i in range(len(seq)):
        if i == len(seq) - 1:
            return len(seq)
        if x >= seq[i] and x <= seq[i+1]:
            return i+1
