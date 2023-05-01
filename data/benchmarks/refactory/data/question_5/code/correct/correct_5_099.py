def top_k(lst, k):
    result = []
    while len(result) < k:
        biggest = lst[0]
        for i in lst:
            if i > biggest:
                biggest = i
        lst.remove(biggest)
        result.append(biggest)
    return result
