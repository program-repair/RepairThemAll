def sort_age(lst):
    a=[]
    for i in lst:
        if i[1]>lst[0][1]:
            a.append(i)
        continue    
    return a
