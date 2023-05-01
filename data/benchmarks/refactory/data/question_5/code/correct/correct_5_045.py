def top_k(lst, k):
    lst_res = lst
    sort = []
    while lst_res:
        largest = lst_res[0]
        for elements in lst_res:
            if elements > largest:
                largest = elements
        lst_res.remove(largest)
        sort.append(largest)
    return sort[:k]
