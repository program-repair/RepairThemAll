def remove_extras(lst):
    if lst == []:
        return []
    sub_list = []
    for elem in lst:
        if elem not in lst[lst.index(elem)+1:]:
            return lst
        elif elem in lst[lst.index(elem)+1:]:
            sub_list += lst[lst.index(elem)+1:]
            while elem in sub_list:
                sub_list.remove(elem)               
            return lst[:lst.index(elem)+1] + sub_list
