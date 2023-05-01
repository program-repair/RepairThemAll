def search(x, seq):
    for i in range(len(seq)):
        if x < seq[i]:
            continue
        elif x >= seq[i]:
            return i
