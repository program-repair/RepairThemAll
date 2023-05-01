def search(x, seq):
    if seq==[]:
        return 0
    for i in range(len(seq)):
        if seq[i]>=x:
            break
        elif seq[-1]<x:
            return len(seq)
    return i
