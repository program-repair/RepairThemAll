def search(x, seq):
    for index, element in enumerate(seq):
        if x <= element:
            return index  
    return len(seq)

