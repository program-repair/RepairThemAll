def remove_extras(lst):
    copy = lst.copy()
    for i in copy:
        if copy.count(i) > 1:
            left = lst[:copy.index(i)+1]
            right = lst[copy.index(i)+1:]
            right.remove(i)
            copy = left + right
    return copy
