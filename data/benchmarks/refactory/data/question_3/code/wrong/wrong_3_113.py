def remove_extras(lst):
    compare = lst[0]
    for element in lst[1:]:
        if element == compare:
            lst.remove(element)
    print(lst)
