def top_k(lst, k):
    n = len(lst) - k
    counter = 0
    while counter < k:
        lst.remove(min(lst))
        counter = counter + 1
    sort_list = []
    while lst != []:
        sort_lst.append(max(lst))
        lst.remove(max(lst))
    return sort_list
    
