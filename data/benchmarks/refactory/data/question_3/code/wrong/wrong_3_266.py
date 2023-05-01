def remove_extras(lst):
    listt = lst.copy()
    listtt = listt.reverse()
    for element in listtt:
        if listtt.count(element) > 1:
            listtt.remove(element)
    return listtt.reverse()
