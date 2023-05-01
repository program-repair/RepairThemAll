def search(x, seq):
    for i in range(len(seq)):
        if x<=seq[i]:
            return i
    return len(seq) #if x is larger then all element in seq
