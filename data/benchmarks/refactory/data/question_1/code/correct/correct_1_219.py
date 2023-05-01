def search(x, seq):
    lst = list(seq)
    lst.append(x)
    sort = []
    while lst:
        smallest = lst[0]
        for ele in lst:
            if ele < smallest:
                smallest = ele
        lst.remove(smallest)
        sort.append(smallest)
    for i in range(len(sort)):
        if sort[i] ==x:
            return i
