def remove_extras(lst):
    if len(lst)==0:
        return lst
    l=[lst[0],]
    for i in lst[1:]:
        if i not in l:
            l+=[i,]
    return l


#qn3
#list1 = [1] * 4
#list2 = [5, 5, 5]
#while not 0:
#    list1[0] += 1
#    if list1[0] == 5: 
#         break          #break out of the while loop
#         list1[1] += 2
#    list1[2] += 3       #list1[2]+=3 every time it loops

#list1=[5, 1, 10, 1]
#list2 is [5, 5, 5]

