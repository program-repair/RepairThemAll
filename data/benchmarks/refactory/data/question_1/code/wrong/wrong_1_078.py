def search(x, seq):
    for count, ele in enumerate(seq):
        if x<=ele:
            return count
        
    for ele in seq:
        if x>ele:
            return len(seq)
