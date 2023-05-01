def search(x, seq):
    list2 = list(enumerate(seq))
    if list2 == []: 
        return 0
    else:
        for i in list2:
            if x <= (i[1]):
                return i[0] 
        return len(seq) 
