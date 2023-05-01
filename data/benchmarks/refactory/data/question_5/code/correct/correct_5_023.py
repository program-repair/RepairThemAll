def top_k(lst, k):
    result=[]
    for i in range(0,k):
        max=lst[0]
        for j in lst:
            if j>max:
                max=j
        result.append(max)
        lst.remove(max)
    return result# Fill in your code here
    pass
