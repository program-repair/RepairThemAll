def sort_age(lst):
    for i in range(1,len(lst)):
        while lst[i][1]<lst[i-1][1]:
            lst.pop(lst[i])
            lst.insert(lst[i],i-1)# Fill in your code here
    return lst.reverse()
