def top_k(lst,k):
    result=[]
    while lst:
        minimum=lst[0]
        for i in lst:
            if i<minimum:
                minimum=i
        result.append(minimum)
        lst.remove(minimum)
    result=result[::-1]
    return result[:k]
