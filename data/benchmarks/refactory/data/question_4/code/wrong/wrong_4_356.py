def sort_age(lst):
    # Fill in your code here
    newlst=[]
    while lst:
        maximum = lst[0][1]
        for i in lst:
            if i[1]>maximum:
                maximum = i[1]
        newlst.append(i)
        lst.remove(i)

    return newlst
