def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0]
        for i in lst:
            if i[1] > biggest[1]:
                biggesr  - i
        lst.remove(biggest)
        sort.append(biggest)
    return sort
    
