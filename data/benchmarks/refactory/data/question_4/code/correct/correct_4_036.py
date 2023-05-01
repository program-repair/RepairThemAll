def sort_age(lst):
    new_lst = []
    while lst:
        max_age = lst[0]
        for tpl in lst:
            if tpl[1] > max_age[1]:
                max_age = tpl
        new_lst.append(max_age)
        lst.remove(max_age)
    return new_lst
    
