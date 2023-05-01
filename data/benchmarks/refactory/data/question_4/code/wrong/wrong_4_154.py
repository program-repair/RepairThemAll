def sort_age(lst):
    new = []
    while lst:
        small = lst[0][1]
        name =lst[0][0]
        for ele in lst:
            if ele[1]>small:
                small = ele[1]
                name = ele[0]
        new.append((name,small))
        lst.remove((name,small))
    return new.reverse
