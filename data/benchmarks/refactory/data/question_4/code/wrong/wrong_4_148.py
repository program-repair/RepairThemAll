def sort_age(lst):
    i=0
    while i+1<len(lst):
        if i[1]<i+1[1]:
            lst.pop(i)
            lst.extend(i)
        else:
            i+=1
    return lst
