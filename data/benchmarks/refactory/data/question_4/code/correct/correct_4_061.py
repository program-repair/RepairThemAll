def sort_age(lst):
    
    sort_lst = []
    
    while lst:
        smallest = lst[0]
        for e in lst:
            if e[1] < smallest[1]:
                smallest = e
        lst.remove(smallest)
        sort_lst.append(smallest)
        
    return sort_lst[::-1]
