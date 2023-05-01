def sort_age(lst):
    a=[]
    while lst:
        biggest=lst[0]
        for i in lst:
            if i >= biggest:
                biggest=i
        lst.remove(biggest)
        a.append(biggest)
    return a
