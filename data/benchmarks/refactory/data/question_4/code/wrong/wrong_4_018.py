def sort_age(lst):
    sample = lst[0]
    newlst = []
    for i in lst:
        if i[1] > sample[1]:
            newlst = [i] + newlst
        else:
            newlst += [i]
    return newlst
