def sort_age(lst):
    for i in range(0,len(lst)):
        this=lst[0]
        for j in range(1,len(lst)+1):
            a=len(lst)-j
            if lst[a][1]>this[1]:
                lst=lst[1:a+1]+[this]+lst[a+1:]
                break
    return lst
