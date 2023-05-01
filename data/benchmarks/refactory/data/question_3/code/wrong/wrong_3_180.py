def remove_extras(lst):
    lst.sort()
    i=0 
    while i<len(lst):
        if i==len(lst)-1:
            break
        elif lst[i]==lst[i+1]:
            lst.remove(lst[i])
        else:
            i+=1
    return lst
