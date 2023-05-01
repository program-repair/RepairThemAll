def top_k(lst, k):
    max_lst =[]
    i = 0
    while i < k:
        max_lst.append(max(lst))
        lst.remove(max(lst))
        i += 1
    return max_lst
