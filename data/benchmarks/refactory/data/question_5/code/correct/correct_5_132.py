def top_k(lst, k):
    klist = []
    while len(klist) < k:
        biggest = lst[0]
        for i in lst:
            if i > biggest:
                biggest = i
        klist.append(biggest)
        lst.remove(biggest)
    return klist
