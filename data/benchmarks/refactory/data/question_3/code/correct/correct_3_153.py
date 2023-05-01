def remove_extras(lst):
    lst_final = []
    for i in lst:
        if i not in lst_final:
            lst_final.append(i)
    return lst_final
