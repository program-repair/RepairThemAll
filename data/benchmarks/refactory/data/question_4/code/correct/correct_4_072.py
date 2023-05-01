def sort_age(lst):
    a = []
    b = lst.copy()
    lst.clear()
    for i in b:
        a += [i[1]]
    for i in range(len(a)):
            for i in range(len(a)):
                if a[i] == min(a):
                    if b[i] not in lst:
                        lst.append(b[i])
                        a[i] = (max(a) +1)
    lst.reverse()                       
    return lst

# sort will work for tuples
