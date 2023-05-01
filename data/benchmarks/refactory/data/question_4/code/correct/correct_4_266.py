def sort_age(lst):
    newlst = []
    while lst:
        maximum = lst[0]
        for i in lst:
            if i[1]>maximum[1]:
                maximum = i
        
        newlst.append(maximum)
        lst.remove(maximum)
    return newlst
