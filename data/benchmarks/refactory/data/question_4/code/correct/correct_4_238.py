def sort_age(lst):
    new_lst = []
    while lst:
        new_lst.append(max_age(lst))
        lst.remove(max_age(lst))
    return new_lst
    
    
def max_age(lst):
    member = lst[0]
    for i in lst:
        if i[1] > member[1]:
            member = i
    return member
