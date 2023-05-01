def search(x, seq):
    for i in range(len(seq)):
        if seq[i]>=x:
            break
        elif seq[-1]<x:
            return len(seq)
    return i
