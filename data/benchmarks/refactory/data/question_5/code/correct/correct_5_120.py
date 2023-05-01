def top_k(lst, k):
    sorted_list = []
    while lst:
        l = lst[0]
        for i in lst:
            if i > l:
                l = i
        lst.remove(l)
        sorted_list.append(l)
    return sorted_list[:k]
