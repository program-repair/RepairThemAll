def remove_extras(lst):
    for i in lst:
        n = lst.index(i)
        lst = lst[:n+1] + list(filter(lambda x: x!=i, lst[n+1:]))
    return lst
                
