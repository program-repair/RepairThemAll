def remove_extras(lst):
    counter = 0
    while counter < len(lst):
        for i in lst[counter + 1:]:
            if lst[counter] == i:
                lst.reverse()
                lst.remove(i)
                lst.reverse()
        counter = counter + 1
    return lst
