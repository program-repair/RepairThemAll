def sort_age(lst):
    old_lst = lst
    new_lst = []
    while old_lst:
        largest = old_lst[0][1]
        remove = old_lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                remove = i
        old_lst.remove(remove)
        new_lst.append(remove)
    return new_lst
