def top_k(lst, k):
    lst = sort_descending(lst)
    return lst[:k-1]
    

def sort_descending(lst):
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            if lst[j][1] > lst[i][1]:
                x = lst[i]
                lst[i] = lst[j]
                lst[j] = x
    return lst
