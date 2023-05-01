def top_k(lst, k):
    new=[]
    for i in range(k):
        biggest=lst[0]
        for element in lst:
            if element>biggest:
                biggest=element
        new.append(biggest)
        lst.remove(biggest)
    return new
