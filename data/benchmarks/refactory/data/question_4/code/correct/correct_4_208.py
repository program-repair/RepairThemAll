def sort_age(lst):
    new = []
    while lst:
        eldest = lst[0]
        for i in lst:
            if i[1] > eldest[1]:
                eldest = i 
        lst.remove(eldest)
        new.append(eldest)
    return new
