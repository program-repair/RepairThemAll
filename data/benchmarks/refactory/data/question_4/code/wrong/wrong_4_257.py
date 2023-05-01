def sort_age(lst):
    a = list(set(lst))
    lst.clear()
    lst.append(a)
    return lst
