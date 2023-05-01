def top_k(lst, k):
    sort = []
    while lst:
        biggest = lst[0]
        for i in lst:
            if i > biggest:
                biggest = i
        lst.remove(biggest)
        sort.append(biggest)
    return sort[0:k]
