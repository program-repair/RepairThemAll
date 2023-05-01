def top_k(lst, k):
    ls=[]
    for i in range(k):
        ls.append(max(lst))
        lst.remove(max(lst))
    return ls
