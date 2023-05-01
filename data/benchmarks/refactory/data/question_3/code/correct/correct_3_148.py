def remove_extras(lst):
    wo_extras = []
    for i in lst:
        if i in wo_extras:
            continue
        wo_extras.append(i)
    return wo_extras
    pass
