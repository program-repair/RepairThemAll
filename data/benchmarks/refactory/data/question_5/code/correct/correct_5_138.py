def top_k(lst, k):
    rs=[]
    for qwerty in range(0,k):
        biggest=lst[0]
        for k in lst:
            if biggest<k:
                biggest=k
        rs.append(biggest)
        lst.remove(biggest)
    return rs
