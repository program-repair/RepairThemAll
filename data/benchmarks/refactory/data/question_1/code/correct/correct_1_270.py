def search(x, seq):
    seq = list(seq)
    for i, elem in enumerate(seq):
        if elem < x:
            continue
        elif elem == x:
            return i 
        elif elem > x:
            return i
    return len(seq)
