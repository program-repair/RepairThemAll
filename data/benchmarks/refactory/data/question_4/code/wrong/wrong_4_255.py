def sort_age(lst):
    newlst = []
    while lst:
        i = lst[0]
        for element in lst:
            if element[1] >= i[1]:
                i = n
        lst.remove(i)
        final.append(i)
    return newlst
