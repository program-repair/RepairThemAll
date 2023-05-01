def sort_age(lst):
    newlist = []
    if lst == []:
        return [] 
    for i in lst : 
        if newlist == []:
            newlist = i 
        elif i[1] > newlist[1] :
            newlist = i 
    lst.remove(newlist)
    return [newlist] + sort_age(lst)
    
    pass
