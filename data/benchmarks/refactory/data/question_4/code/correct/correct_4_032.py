def sort_age(lst):
    sort_list = []
    while lst: # a is not []
        biggest = lst[0]
        for element in lst:
            if element[1] > biggest[1]:
                biggest = element
        lst.remove(biggest)
        sort_list.append(biggest)
    return sort_list
