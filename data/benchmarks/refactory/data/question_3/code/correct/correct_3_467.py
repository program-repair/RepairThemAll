def remove_extras(lst):
    new_lst = []
    added = set()
    for val in lst:
        if not val in added:
            new_lst.append(val)
            added.add(val)
    return new_lst
