def remove_extras(lst):
    listt = []
    for i in lst:
        if i in listt:
            continue
        else:
            listt += [i]
    return listt
