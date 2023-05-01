def magus_sort(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] >= lst[1]:
            return lst
        else:
            return [lst[1], lst[0]]
    else:
        if lst[0] >= lst[1]:
            list1, list2 = [lst[0]], [lst[1]]
        else:
            list1, list2 = [lst[1]], [lst[0]]
        for i in lst[2:]:
            if i >= list1[0]:
                list1.append(i)
            else:
                list2.append(i)
        return magus_sort(list1) + magus_sort(list2)

def top_k(lst, k):
    return magus_sort(lst)[0:k]
