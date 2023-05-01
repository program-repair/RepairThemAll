def top_k(lst, k):
    for i, e in enumerate(lst):
        mx = max(range(i,len(lst)), key= lambda x: lst[x])
        lst[i], lst[mx] = lst[mx], e
    return lst[:k]
