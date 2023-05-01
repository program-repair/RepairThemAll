def remove_extras(lst):
    for i in range(len(lst)):
        print(lst[i:])
        print(lst[i:].count(lst[i]))
        if lst.count(lst[i]) > 1:
            element = lst[i]
            lst.reverse()
            lst.remove(element)
            lst.reverse()
    return lst
                
