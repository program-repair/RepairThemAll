def search(x, seq):
    position = 0
    while position < len(seq)-1:
        if seq[position] == x:
             break
        elif seq[position] > x:
            break
        position = position + 1
    if seq[position] < x:
        position = position + 1
    return position
