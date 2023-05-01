def search(x, seq):
    position = 0
    for i in range(len(seq)):
        if x > seq[i]:
            position = position+1
        
    return position
