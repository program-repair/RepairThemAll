def sort_age(lst):
    newlist=[]
    newlist2=[]
    for elements in lst:
        newlist.append(elements)
    
    while newlist:
        largest = newlist[0]
        for elements in newlist:
            print (largest)
            if largest[1]<elements[1]:
                largest = elements
        newlist2.append(largest)
        newlist.remove(largest)
    
    return newlist2
    pass
