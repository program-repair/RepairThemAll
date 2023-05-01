def top_k(lst, k):
    newlst=[]
    while lst:
        largest=lst[0]
        for i in lst:
            if largest<i:
                largest=i
        newlst.append(largest)
        lst.remove(largest)
    return newlst[:k]
    
   
