def top_k(lst, k):
    sort = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        sort.append(largest)
        lst.remove(largest)
    top = sort[:k]
    return top
