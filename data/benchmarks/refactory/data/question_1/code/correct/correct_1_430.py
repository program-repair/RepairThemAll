def search(x, seq):
    index = 0
    while index < len(seq):
        if x <= seq[index]:
            break
        else:
            index += 1
    return index
    
