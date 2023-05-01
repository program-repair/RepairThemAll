def quicksort(lst, f):
    if len(lst) <= 1:
        return lst

    pivot_ind = len(lst)//2
    pivot = lst[pivot_ind]

    flist, blist = [], []
    for i in range(len(lst)):
        if i == pivot_ind:
            continue
        if f(lst[i]) <= f(pivot):
            flist.append(lst[i])
        else:
            blist.append(lst[i])
    
    finalsort = quicksort(flist, f) + [pivot] + quicksort(blist, f)
    return finalsort

def sort_age(lst):
    return quicksort(lst, lambda x: x[1])[::-1]
