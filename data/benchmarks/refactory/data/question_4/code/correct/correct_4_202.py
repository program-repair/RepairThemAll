def sort_age(lst):
    l=lst.copy()
    res=[]
    while l:
        biggest=l[0]

        for element in l:
            if element[1]>biggest[1]:
                biggest=element
                
        l.remove(biggest)
        res.append(biggest)
    return res
