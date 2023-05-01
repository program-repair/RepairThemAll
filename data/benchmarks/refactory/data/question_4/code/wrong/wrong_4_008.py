def sort_age(lst):
    for i in range(0,len(lst)):
        this=lst[i]
        for j in range(0,len(lst)):
            if lst[j][1]<this[1]:
                del lst[i]
                lst=lst[0:j]+[this]+lst[j:]
    return lst# Fill in your code here
    pass
