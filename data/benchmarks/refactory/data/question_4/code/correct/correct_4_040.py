def sort_age(lst):
    for i in range(0,len(lst)):
        this=lst[i]
        j=0
        while j<i:
            if this[1]>lst[j][1]:
                break
            j+=1
        del lst[i]
        lst.insert(j,this)
    return lst
    
