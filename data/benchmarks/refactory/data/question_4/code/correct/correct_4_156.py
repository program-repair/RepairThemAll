def sort_age(lst):
    new_list = []
    while lst:
        smallest = lst[0]
        for element in lst:
            if smallest[1]<element[1]:
                smallest = element
        lst.remove(smallest)
        new_list.append(smallest)
    return new_list
                
        
