def sort_age(lst):
    i=0
    while i+1<len(lst):
        if lst[i][1]<lst[i+1][1]:
            lst.extend([lst[i]])
            lst.pop(lst[i])
        else:
            i+=1
    return lst
