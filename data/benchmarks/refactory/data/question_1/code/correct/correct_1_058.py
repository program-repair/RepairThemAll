def search(x, seq):
    lst = list(seq)
    if lst == []:
        lst.append(x)
    else:
        for i in range(len(lst)):
            if x < lst[i]:
                lst.insert(i,x)
            else:
                lst.insert(len(lst),x)
    for i in range(len(lst)):
         if lst[i] == x:
             return i
