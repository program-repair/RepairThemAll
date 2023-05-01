def remove_extras(lst):
    new_lst = []
    for num in lst:
        if num not in new_lst:
            new_lst.append(num)
    return new_lst
