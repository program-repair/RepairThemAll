def search(x, seq):
    if x >= seq[len(seq)-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x > seq[i]:
                continue
            else:
                return i
