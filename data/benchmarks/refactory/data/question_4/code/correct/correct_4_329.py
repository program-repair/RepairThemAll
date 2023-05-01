def sort_age(lst):
    new_list = []
    while lst:
        biggest = lst[0]
        for item in lst:
            if item[1] > biggest[1]:
                biggest = item
        lst.remove(biggest)
        new_list.append(biggest)
    return new_list
