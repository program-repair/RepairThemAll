def top_k(lst, k):
    sorted = []
    while lst:
        biggest = lst[0]
        for elem in lst:
            if elem > biggest:
                biggest = elem
        lst.remove(biggest)
        sorted.append(biggest)
    return sorted[:k]
