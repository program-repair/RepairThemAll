def sort_age(lst):
    result=[] 
    while lst:
        largest=lst[0][1]
        tuple_largest=lst[0]
        for i in lst:
            if i[1]>largest:
                largest=i[1]
                tuple_largest=i
        lst.remove(tuple_largest)
        result.append(tuple_largest)
    return result
