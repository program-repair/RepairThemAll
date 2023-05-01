def sort_age(lst):
    sort=[]
    while lst:
        biggest=lst[0][1]
        for i in range(len(lst)):
            count=0
            if lst[i][1]>=biggest:
                biggest=lst[i][1]
            else:
                i+=1
                count+=1
        lst.remove(lst[i-count])
        sort.append(lst[i-count])
    return sort# Fill in your code here
    
