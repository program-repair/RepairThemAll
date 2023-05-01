def sort_age(lst):
    result=[] 
    while lst:
        biggest=lst[0][1]
        tuple_biggest=lst[0]
        for i in lst:
            if i[1]>biggest:
                biggest=i[1]
                tuple_biggest=i
        lst.remove(tuple_biggest)
        result.append(tuple_biggest)
    return result
