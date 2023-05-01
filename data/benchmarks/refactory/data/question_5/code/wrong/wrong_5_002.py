def top_k(lst, k):
    lst_res = lst
    sort = []
    while lst_res:
        largest = lst_res[0]
        for elements in lst_res:
            if element > largest:
                largest = element
        lst_res.remove(largest)
        sort.append(largest)
    return sort[:k]
