def sort_age(lst):
    newlst = []
    ages = []
    for i in lst:
        ages.append(i[1])
    ages.sort()
    for x in ages[::-1]:
        for i in lst:
            if i[1] == x:
                newlst.append(i)
    return newlst
        
