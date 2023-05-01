def sort_age(lst):
    if lst == []:
        return new
    new = []
    small = lst[0][1]
    for i in range(1,len(lst)):
        if lst[i][1]<small:
            small = lst[i][1]
    new.append(small)
    lst.remove(small)
    sort_age(lst)
