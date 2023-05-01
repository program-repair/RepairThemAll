def top_k(lst,k):
    sort_list = []
    while lst:
        biggest = lst[0]
        for e in lst:
            if biggest < e:
                biggest = e
        lst.remove(biggest)
        sort_list.append(biggest)
    return sort_list[:k]
