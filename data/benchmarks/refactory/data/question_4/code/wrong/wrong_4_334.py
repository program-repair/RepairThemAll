def sort_age(lst):
    for i in range(1,len(lst)):
        while lst[i][1]<lst[i-1][1]:
            lst.pop(i)
            lst.insert(i-1,lst[i])# Fill in your code here
    return lst.reverse()
