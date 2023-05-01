def sort_age(lst):
    new_list = []
    while lst:
        eldest = lst[0]
        for i in lst:
            if i[1] > eldest[1]:
                eldest = i
        lst.remove(eldest)
        new_list.append(eldest)
    return new_list
