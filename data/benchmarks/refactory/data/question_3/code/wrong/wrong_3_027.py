def remove_extras(lst):
    result = []
    counter = 0
    while counter < len(lst):
        for i in lst[1:]:
            if lst[counter] == i:
                lst = ((lst.reverse()).remove(i)).reverse()
        counter = counter + 1
    return lst
                
