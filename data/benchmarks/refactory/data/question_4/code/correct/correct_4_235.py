def sort_age(lst):
    new_lst = []

    while lst:
        big_age = lst[0]
        for i in lst:
            if i[1] > big_age[1]:
                big_age = i
        lst.remove(big_age)
        new_lst.append(big_age)
    return new_lst
