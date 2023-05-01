def remove_extras(lst):
    listt = lst.reverse()
    for element in listt:
        if listt.count(element) > 1:
            listt.remove(element)
    return listt.reverse()
