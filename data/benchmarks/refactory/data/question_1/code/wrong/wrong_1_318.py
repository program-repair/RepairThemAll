def search(x, seq):
    n = len(seq)
    for i in range(n):
        next_element = seq[i]
        if x > next_element:
            return 0
        else:
            return i
    return n        
            
