def sort_age(lst):
    if len(lst) == 1:
        return lst
    elif lst == []:
        return []
    else:
        s = 0
        for i in lst:
            if i[1] > s:
                s = i[1]
                t = i
        lst.remove(t)
        return [t] + sort_age(lst)
        
