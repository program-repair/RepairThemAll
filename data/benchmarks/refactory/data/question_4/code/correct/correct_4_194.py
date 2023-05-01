def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0]
        for e in lst:
            print(e)
            if e[1] > biggest[1]:
                biggest = e
        lst.remove(biggest)
        sort.append(biggest)
    return sort

