def search(x, seq):
    a = 0
    for ele in seq:
        if ele < x:
            a +=1
    return a
