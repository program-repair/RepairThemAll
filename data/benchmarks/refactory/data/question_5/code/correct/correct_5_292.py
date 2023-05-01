def top_k(lst, k):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] > lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst[:k]
