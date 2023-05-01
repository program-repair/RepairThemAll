def sort_age(lst):
    a = []
    b = []
    n = len(lst)
    for i in range(n):
        age = lst[i][1]
        a += [age]
        a.sort()
        a.reverse()
    for j in range(n):
        for k in range(n):
            if a[j] == lst[k][1]:
                b += [lst[k]]
            else:
                continue
    return b
