def sort_age(lst):
    new = []
    while lst:
        curr = lst[0]
        for i in lst:
            if i[1]>curr[1]:
                curr = i
        lst.remove(curr)
        new.append(curr)
        
    return new


