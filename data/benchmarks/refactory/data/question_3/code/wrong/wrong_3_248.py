def remove_extras(lst):
    newLst=[]
    hashtable=[]
    for i in lst:
        if hashtable[lst[i]]!=1:
            hasttable[lst[i]]=1
            newLst.append(lst[i])
            
        
    return newLst
