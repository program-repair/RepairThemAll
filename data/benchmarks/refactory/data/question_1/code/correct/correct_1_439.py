def search(x, seq):
    position = 0
    while position < len(seq):
        if seq[position] == x:
             break
        elif seq[position] > x:
            break
        position = position + 1
    return position
