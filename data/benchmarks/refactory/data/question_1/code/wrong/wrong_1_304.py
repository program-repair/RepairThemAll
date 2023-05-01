def search(x, seq):
    if type(seq) == list:
        a = seq.copy()
        a.append(x)
        a.sort()
        for i, elem in enumerate(a):
            if elem == x:
                return i
    else:
        temp_tuple = seq.copy()
        temp_tuple+=(x,)
        for i, elem in enumerate(sorted(temp_tuple)):
            if elem == x:
                return i
