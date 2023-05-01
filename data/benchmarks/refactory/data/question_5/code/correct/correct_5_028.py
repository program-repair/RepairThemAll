
def top_k(lst, k):
    sort = []
    while lst:
        biggest = lst[0]
        for elem in lst:
            if elem > biggest:
                biggest = elem
        lst.remove(biggest)
        sort.append(biggest)
    return sort[:k]

