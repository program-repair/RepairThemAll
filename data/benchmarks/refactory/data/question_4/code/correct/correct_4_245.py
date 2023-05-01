def sort_age(lst):
    for i, e in enumerate(lst):
        mx = max(range(i,len(lst)), key= lambda x: lst[x][1])
        lst[i], lst[mx] = lst[mx], e
    return lst
