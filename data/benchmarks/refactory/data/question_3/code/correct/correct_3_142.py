def remove_extras(lst):
    # your code here
    lst_new = []
    for element in lst:
        if element not in lst_new:
            lst_new.append(element)
    return lst_new
