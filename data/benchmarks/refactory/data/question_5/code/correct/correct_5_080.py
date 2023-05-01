def top_k(lst, k):
    # Fill in your code here
    sorted = []
    
    while lst:
        smallest = lst[0] # smallest has to exist within this step
        for i in lst:
            if i < smallest:
                smallest = i # take note: you must not reverse this step
    
        sorted.append(smallest)
        lst.remove(smallest)
        
    #ends the while loop, when lst has no elements
    # and every element is sorted into sorted
    sorted.reverse() 
    
    return sorted[0:k]
