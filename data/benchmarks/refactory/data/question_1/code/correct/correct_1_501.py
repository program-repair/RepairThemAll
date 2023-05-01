def search(x, seq):
    n = len(seq)
    for i in range(n):
        next_element = seq[i]
        if x <= next_element:
            return i
    return n
