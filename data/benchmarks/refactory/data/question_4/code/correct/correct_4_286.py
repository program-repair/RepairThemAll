def sort_age(lst):
    new_lst = []
    while lst:
        max_num = lst[0]
        for i in lst:
            if i[1] > max_num[1]:
                max_num = i
        lst.remove(max_num)
        new_lst.append(max_num)
    return new_lst
