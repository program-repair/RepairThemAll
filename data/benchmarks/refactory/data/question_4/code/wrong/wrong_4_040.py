def sort_age(lst):
    
    sort_lst = []
    
    while lst:
        smallest = lst[0]
        for element in lst:
            if element[1] < smallest[1]:
                smallest = element
        lst.remove(smallest)
        sort_lst.append(smallest)
    return sort_lst.reverse()
    
