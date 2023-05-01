def search(x, seq):
    for i in range(len(seq)-1):
        if x > seq[i] and x <= seq[i+1]:
            return i+1
    return None
