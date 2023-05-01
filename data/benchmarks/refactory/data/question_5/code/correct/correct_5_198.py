def top_k(lst, k):
    l=lst.copy()
    res=[]
    while len(res)<k and l :
        biggest=l[0]

        for element in l:
            if element>biggest:
                biggest=element
                
        l.remove(biggest)
        res.append(biggest)
    return res

