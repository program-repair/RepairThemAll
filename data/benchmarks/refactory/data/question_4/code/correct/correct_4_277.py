def sort_age(lst):
    # Fill in your code here
    new_lst = []
    while lst:
        largest = lst[0]
        for element in lst:
            if largest[1] < element[1]:
                largest = element
        lst.remove(largest)
        new_lst.append(largest)
    return new_lst
        
