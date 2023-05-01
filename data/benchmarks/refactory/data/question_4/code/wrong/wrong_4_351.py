def sort_age(lst):
    lst.sort()
    new = []
    for i in range(len(lst)):
        j = len(lst) - i- 1
        new.append(lst[j])
    return new
