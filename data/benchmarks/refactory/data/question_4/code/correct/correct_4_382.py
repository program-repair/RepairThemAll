def sort_age(lst):
    new_lst = []

    while lst:
        max_age = lst[0]  # arbitrary number in list 
        for x in lst: 
            if x[1] > max_age[1]:
                max_age = x
        new_lst.append(max_age)
        lst.remove(max_age)
    return new_lst
