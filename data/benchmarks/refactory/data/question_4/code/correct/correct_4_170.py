def sort_age(lst):
    new = []
    while lst:
        Max = max(lst,key = lambda x : x[1])
        new.append(Max)
        lst.remove(Max)
    return new
    
