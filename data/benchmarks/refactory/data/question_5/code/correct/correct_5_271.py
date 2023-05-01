def top_k(lst, n):
    for j in range(len(lst)):
            maxi=lst[j]
            for k in range(j+1,len(lst)):
                if lst[k]>maxi:
                    maxi=lst[k]
                    lst[j],lst[k]=lst[k],lst[j]
            result=lst[0:n]
    return result
