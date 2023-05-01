def search(x, seq):
    n = len(seq)
    if seq: #if seq is not an empty list/tuple
        for i in range(n):
            next_element = seq[i]
            if x <= next_element:
                return i
        return n  
