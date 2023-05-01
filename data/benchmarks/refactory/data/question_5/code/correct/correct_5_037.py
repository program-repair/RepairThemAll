def top_k(lst, k):
    sort_list = []
    counter = 0
    while counter < k:
        sort_list.append(max(lst))
        lst.remove(max(lst))
        counter = counter + 1
    return sort_list
    
