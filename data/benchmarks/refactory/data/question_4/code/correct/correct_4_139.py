def sort_age(lst):
    if len(lst) < 2:
        return lst
    for j in range(len(lst)-1):
        minimum = j
        for i in range(j+1, len(lst)):
            if lst[minimum][1] > lst[i][1]:
                minimum = i
        lst[j], lst[minimum] = lst[minimum], lst[j]
    lst.reverse()
    return lst
