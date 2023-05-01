def remove_extras(lst):
    a = ()
    n = len(lst)
    for i in range(n):
        for j in range(i,n):
            if lst[i] == lst[j] and i != j:
                a += (lst[j],)
            else:
                continue
    c = a[:-1]
    b = lst[::-1]
    for i in range(len(c)):
        b.remove(c[i])
    d = b[::-1]
    return d
