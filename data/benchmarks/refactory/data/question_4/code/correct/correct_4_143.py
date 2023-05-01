def sort_age(lst):
    sort=[]
    while lst:
        largest=lst[0]
        for i in lst:
            if i[1]>largest[1]:
                largest=i
        lst.remove(largest)
        sort.append(largest)
    return sort

#    lst.sort(key= lambda x:x[1], reverse=True)
 #   return lst
