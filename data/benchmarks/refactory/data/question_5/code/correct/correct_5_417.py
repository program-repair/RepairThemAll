def top_k(lst, k):
    result=[]
    while k>0:
        result.append(max(lst))
        lst.remove(max(lst))
        k=k-1
    return result
