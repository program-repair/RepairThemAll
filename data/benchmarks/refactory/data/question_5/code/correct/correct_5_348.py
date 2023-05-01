def top_k(lst, k):
    for i in range(0,len(lst)-1): 
            for j in range(i+1,len(lst)): 
                if lst[i]<lst[j]:  
                    lst[i],lst[j]=lst[j],lst[i]
    return lst[0:k]
