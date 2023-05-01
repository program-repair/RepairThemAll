def sort_age(lst):
    sort =[]
    while lst:
        biggest = lst[0]
        for i in lst:
            if int(i[1])> biggest[1]:
                biggest = i
        lst.remove(biggest)
        sort.append(biggest)
    return sort
    pass
