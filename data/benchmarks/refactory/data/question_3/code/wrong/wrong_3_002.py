def remove_extras(lst):
    # your code here
    occurrences = ()
    new_lst = []
    for item in lst:
        if item not in occurrences:
            occurences += (item,)
            new_list.append(item)
    return new_lst
