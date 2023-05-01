def sort_age(lst):
    sort=[]
    while lst:
        largest=lst[0][1]
        for i in lst:
            if i[1]>largest:
                largest=i[1]
        lst.remove(i)
        sort.append(i)
    return sort 
