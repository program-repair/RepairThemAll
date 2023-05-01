def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0]
        for k in lst:
            if k[1] > biggest[1]:
                biggest = k
        lst.remove(biggest)
        sort.append(biggest)
