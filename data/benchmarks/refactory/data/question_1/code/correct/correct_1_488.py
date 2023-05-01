def search(x, seq):
    if not seq:
        return 0
    else:
        for i in range(len(seq)):
            if x<=seq[i]:
                return i
    return i+1
