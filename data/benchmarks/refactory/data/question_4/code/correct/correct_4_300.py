def sort_age(lst):
    for i in range(0,len(lst)):
        for y in range(1+i,len(lst)):
            if lst[y][1] > lst[i][1]:
                lst[y],lst[i] = lst[i],lst[y]
    return lst
    
#alt

#def sort_age(lst):
    #sort = []
    #while lst:
        #biggest = lst[0]
        #for people in lst:
            #if people[1] > biggest[1]:
                #biggest = people
        #lst.remove(biggest)
        #sort.append(biggest)
    #return sort
