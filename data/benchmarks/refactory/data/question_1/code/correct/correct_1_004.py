def search(x, seq):
    index = 0
    for i in range(0,len(seq)):
        if x > seq[i]:
            index = i + 1
    return index
