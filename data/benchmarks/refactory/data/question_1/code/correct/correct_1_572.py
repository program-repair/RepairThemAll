def search(x, seq):
    for position, elem in enumerate(seq):
        if x <= elem:
            return position #position to insert x
    return len(seq)
            
