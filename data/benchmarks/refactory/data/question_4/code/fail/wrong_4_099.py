def sort_age(lst):
    for i in range(len(lst)-1):
        while lst[i][1] < lst[i+1][1]:
            temp = lst[i]
            del lst[i]
            lst += [temp]
    return lst
