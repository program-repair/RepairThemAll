def sort_age(lst):
    sort = []
    while lst: 
        biggest = lst[0][1]
        element=lst[0]
        for ele in lst:
            if ele[1] > biggest:
                biggest = ele[1]
                element=ele
        lst.remove(element)
        sort.append(element)
    return sort
