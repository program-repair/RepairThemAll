def quicksort(lst, f, comparator):
    if len(lst) <= 1:
        return lst
        
    pivot_index = len(lst) // 2
    pivot = lst[pivot_index]
    flist, blist = [], []
    
    for i in range(len(lst)):
        if i == pivot_index:
            continue
        if comparator(f(lst[i]), f(pivot)):
            flist.append(lst[i])
        else:
            blist.append(lst[i])
    
    return quicksort(flist, f, comparator) + [pivot] + quicksort(blist, f, comparator)

def top_k(lst, k):
    sorted_lst = quicksort(lst, lambda x: x, lambda x, y: x > y)
    return sorted_lst[:k]
