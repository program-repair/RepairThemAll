def remove_extras(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
        if new_lst.count(i) > 1:
            new_lst.pop()
            continue
    return new_lst
