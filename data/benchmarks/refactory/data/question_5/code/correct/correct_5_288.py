def sort_list(lst):
    if len(lst) < 2:
        return lst
    for j in range(len(lst)-1):
        minimum = j
        for i in range(j+1, len(lst)):
            if lst[minimum] > lst[i]:
                minimum = i
        lst[j], lst[minimum] = lst[minimum], lst[j]
    lst.reverse()
    return lst 
    
def top_k(lst, k):
    a = sort_list(lst)
    return a[0:k]
