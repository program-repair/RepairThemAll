def search(x, seq):
    if x>=max(seq):
        return len(seq)
    else:
        for i in range(len(seq)):
            if x<=seq[i]:
                return i
                break
            else:
                continue
