#def sort_age(lst):
    # Fill in your code here
    #lst.sort(key = lambda x: x[1], reverse = True) #running an operation to mutate the list
    #return lst
    
def sort_age(lst):
    # Fill in your code here
    sort = []
    n = len(lst)
    
    for i in range(n):
        smallest = lst[0] #create a variable called "smallest"
        for element in lst: #loop through each element in list
            if element[1] < smallest[1]: #must compare by the same property of element
                smallest = element
        lst.remove(smallest)
        sort.append(smallest)
    
    
    sort.reverse() #reverse the list that is sorted
    return sort
    
def sort_age2(lst):
    sort = []
    while lst: #while there is something in the list
        smallest = lst[0]
        for element in lst:
            if element[1] < smallest[1]:
                smallest = element
        lst.remove(smallest)
        sort.append(smallest)
    
    sort.reverse()
    return sort
        
