def top_k(lst, k):
    a=[]
    for i in range (0,k):
        a=a+[max(lst)]
        lst.remove(max(lst))
    
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] > a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a
        
