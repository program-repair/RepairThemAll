def search(x, seq):
    if type(seq) == list:
        a = seq.copy()
        a.append(x)
        a.sort()
        for i, elem in enumerate(a):
            if elem == x:
                return i
    else:
        temp_list = list(seq)
        temp_list.append(x,)
        temp_list.sort()
        for i, elem in enumerate(temp_list):
            if elem == x:
                return i
