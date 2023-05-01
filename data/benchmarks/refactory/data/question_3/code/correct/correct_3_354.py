def remove_extras(lst):
    lst.reverse()
    for elem in lst:
        while elem in lst[lst.index(elem)+1:]:
            lst.remove(elem)
            #reversing list to remove elements from the back.. I think?
    lst.reverse()
    new_lst = lst.copy()
    return new_lst


