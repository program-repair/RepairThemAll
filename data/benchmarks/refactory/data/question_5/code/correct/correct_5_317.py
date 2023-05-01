def top_k(lst, k):
    for j in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i]<lst[1+i]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst[:k]
