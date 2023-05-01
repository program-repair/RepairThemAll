def sort_age(lst):
    if lst==[]:
        return []
    sort=[]
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        sort.append(largest)
    return sort
    pass


