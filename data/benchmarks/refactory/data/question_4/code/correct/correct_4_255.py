def func(lst, x):
    index = len(lst)
    for i in range(len(lst)):
        if lst[i][1] < x:
            continue
        else:
            index = i
            break
    return index
    
def sort_age(lst):
    newlist = []
    for i in range(len(lst)):
        age = lst[i][1]
        b = func(newlist, age)
        newlist.insert(b, lst[i])
    return list(reversed(newlist))
    
