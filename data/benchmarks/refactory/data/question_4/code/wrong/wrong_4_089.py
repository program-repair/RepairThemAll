def sort_age(lst):
    holder=[]
    if lst==[]:
        return []
    for x in lst:
        if holder==[]:
            holder=x
        elif x[1]>holder[1]:
            holder=x
    return holder+sort_age(lst[1:])

