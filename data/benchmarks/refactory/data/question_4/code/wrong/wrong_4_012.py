def sort_age(lst):
    old_lst = lst
    new_lst = []
    while old_lst:
        largest = old_lst[0]
        for i in lst:
            if i > largest:
                largest = i
        old_lst.remove(largest)
        new_lst.append(largest)
    return new_lst
