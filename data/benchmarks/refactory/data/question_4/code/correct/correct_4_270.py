def sort_age(lst):
    for i in range(len(lst)):
        maxi=lst[i][1]
        for j in range (i+1,len(lst)):
            if lst[j][1]>maxi:
                maxi=lst[j][1]
                lst[i],lst[j]=lst[j],lst[i]
                
    return lst
