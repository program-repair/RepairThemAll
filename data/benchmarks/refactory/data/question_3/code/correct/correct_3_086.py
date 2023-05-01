def remove_extras(lst):
    # your code here
    new_lst = []
    for i in lst:
        if not i in new_lst:
            new_lst.append(i)
    return new_lst
